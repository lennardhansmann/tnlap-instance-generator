# TNLAP Instance Generator

A parameterized instance generator for the **Template-based Newspaper Layout
Assignment Problem (TNLAP)**. It produces synthetic but structurally realistic
instances, enabling experiments
on the TNLAP without access to proprietary production data.

The modeling rationale and parameter choices are described in the accompanying
papers.

## Installation

Clone the repository and ensure Python 3.9+ is installed.

## Usage

The generator requires the following instance-specific parameters.

| Parameter  | Description | Values |
|------------|-------------|---------|
| `pages`    |  $\|P\|$        | integer > 0 |
| `articles` |  $\|A\|$     | integer > 0 |
| `type`     | instance type  | `A`, `B` |
| `seed`     | seed       | integer |


### As a command-line tool

Generate a instance:

```bash
python -m tnlap_gen.cli create --pages 10 --articles 50 --type A --seed 133
```

### As a library

```python
from tnlap_gen import create_instance, save_instance

instance = create_instance(n_pages=10, n_articles=50, shell_type="A", seed=133)
save_instance(instance, "instance.json")
```

For full control over the parameters, pass an explicit configuration:

```python
from tnlap_gen import GeneratorConfig, create_instance

config = GeneratorConfig(shell_type="B", shells_per_box=(4, 10))
instance = create_instance(n_pages=20, n_articles=100, config=config)
```


### Instance naming convention

Generated benchmark instances follow the naming convention

`P<pages>_A<articles>_<type>_<seed>`

For example,

`P10_A50_A_133.json`

denotes an instance with 10 pages, 50 articles, shell type `A`, and random seed `133`.



## Parameters

The following default parameter values are used by the instance generator.

| Parameter             | Description               | Default         |
|-----------------------|---------------------------|-----------------|
| `layouts_per_page`    | candidate layouts / page  | (10, 20)        |
| `boxes_per_layout`    | boxes / layout            | (3, 5)          |
| `shells_per_box`      | shells / box              | (6, 15)         |
| `reuse_probability`   | layout reuse probability  | 0.1             |
| `shell_max_fraction`  | shell max as box fraction | (0.75, 1.0)     |
| `article_length`      | article length (chars)    | (500, 20000)    |
| `priority_a_fraction` | share of priority A       | (0.10, 0.20)    |
| `priority_b_fraction` | share of priority B       | (0.30, 0.40)    |

## Instance format

Each instance is a JSON object. Field names follow the convention 

`<content>_<key1>_<key2>_...`

where `<content>` denotes the stored information and the subsequent terms denote the indexing keys from outermost to innermost level. For example, `shells_layout_box` stores shell ids indexed by layout and box.

| Field                 | Description                                                |
|-----------------------|------------------------------------------------------------|
| `n_pages`    | number of pages    |
| `n_layouts`  | number of layouts  |
| `n_articles` | number of articles |
| `n_shells`   | number of shells   |
| `layouts_page`       | list of master layout ids available on page                              |
| `boxes_layout`         | list of box ids per master layout                                         |
| `geometry_layout_box` | per box: position `x,y`, size `w,h`, max char capacity         |
| `shells_layout_box`   | list of shell ids per (layout, box)                                |
| `shells_article`      | list of shell ids per article                           |
| `length_article`      | article length in characters                               |
| `params_shell`        | per shell: `min`/`max` admissible character count          |
| `priority_article`    | priority tier (`A`/`B`/`C`) per article                    |
| `sections`            | number of sections                                        |
| `articles_section`    | list of article ids per section                                    |
| `sections_page`       | list of section ids per page                         |




## Reproducibility

All randomness is driven by a single seeded generator, so a given
`(n_pages, n_articles, shell_type, seed)` always yields an identical instance.

## Citation

If you use this generator, please cite the accompanying paper. 

## License

Released under the MIT License. See [`LICENSE`](LICENSE).
