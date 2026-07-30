"""Command-line interface for the TNLAP instance generator.

Examples
--------
Generate a single instance::

    python -m tnlap_gen.cli create --pages 10 --articles 50 --type A --seed 133

"""

from __future__ import annotations

import argparse
from typing import List, Tuple

from .generator import create_instance, save_instance



def _instance_name(n_pages: int, n_articles: int, shell_type: str, seed: int) -> str:
    return f"P{n_pages}_A{n_articles}_{shell_type}_{seed}.json"


def cmd_single(args: argparse.Namespace) -> None:
    instance = create_instance(
        n_pages=args.pages,
        n_articles=args.articles,
        shell_type=args.type,
        seed=args.seed,
    )
    path = args.out or _instance_name(args.pages, args.articles, args.type, args.seed)
    save_instance(instance, path)
    print(f"Wrote {path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tnlap_gen",
        description="Parameterized instance generator for the TNLAP.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_single = sub.add_parser("create", help="generate one instance")
    p_single.add_argument("--pages", type=int, required=True)
    p_single.add_argument("--articles", type=int, required=True)
    p_single.add_argument("--type", choices=("A", "B"), default="A")
    p_single.add_argument("--seed", type=int, default=0)
    p_single.add_argument("--out", type=str, default=None, help="output path")
    p_single.set_defaults(func=cmd_single)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
