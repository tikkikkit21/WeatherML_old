# Experiment & Dataset Log

## Experiment Log
### Result Overview
| Experiment | Train Acc. | Test Acc. |
| ---------- | ---------- | --------- |
| Exp 1      | 73.47%     | 81.82%    |
| Exp 22     | 79.14%     | 73.68%    |

### Experiment 1
- **Date:** 01/27/2024
- **Train Acc:** 73.47%
- **Test Acc:** 81.82%

First experiment with some initial training data. The purpose of this is to
ensure my code can return results as well as playing around with some different
visualization strategies. Overall not a bad start, with ~81% test accuracy and a
decent looking scatter plot for temperature.

### Experiment 2
- **Date:** 02/24/2024
- **Train Acc:** 79.14%
- **Test Acc:** 73.68%

Second run was mainly to test that my program can dynamically switch between
dataset versions. There was also more data to train on so I was curious to see
how it would fare. There was a ~2% decrease in accuracy, which I'm guessing is
due to the uneven distribution of label records. It's still winter so there's a
lot of `coat` records in there, which may be skewing results a little. There's
also a new data feature `Gust` since iOS Weather added it. However, it has
missing data so I ignored it for now.

# Dataset Log
Google sheets: https://docs.google.com/spreadsheets/d/1wjoOM3OyRlOUdET7_jU2uoCyOraQOWY8XGOw8LVWK3A

## Training Results
| Version | Train Acc. | Test Acc. |
| ------- | ---------- | --------- |
| v1      | 73.47%     | 81.82%    |
| v2      | 79.14%     | 73.68%    |

## Dataset Notes
### Version 1 (01/27/2024)
- 109 entries
- Development purposes
    - Test out training model
    - Generate some initial visualizations

### Version 2 (02/24/2024)
- 182 entries
- Development purposes
    - Add metadata for different dataset versions
    - Programs can dynamically adjust based on provided version
- Added `Gusts` data
    - Missing values
    - Train without gust data for now
