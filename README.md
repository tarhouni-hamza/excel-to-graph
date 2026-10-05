# Excel to Graph

A Python project that reads an Excel file and automatically creates graphs such as bar charts, line charts, scatter plots, histograms, and correlation heatmaps.

## Features

- Reads `.xlsx` Excel files
- Detects numeric, date, and categorical columns automatically
- Creates multiple charts automatically
- Saves charts as PNG files
- Shows charts in popup windows on Windows

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Run the script

```bash
python datagraph.py "your_file.xlsx"
```

Optional sheet name or index:

```bash
python datagraph.py "your_file.xlsx" "Sheet1"
```

or

```bash
python datagraph.py "your_file.xlsx" 0
```

## Output files

The script creates files like:

- `graph_bar.png`
- `graph_line.png`
- `graph_scatter.png`
- `graph_hist.png`
- `graph_corr.png`

## Example

```bash
python datagraph.py "Leads in Eu.xlsx"
```

## Notes

- If your Excel file has spaces in the name, wrap it in quotes.
- The script uses the `TkAgg` Matplotlib backend so graphs can appear in popup windows on Windows.
