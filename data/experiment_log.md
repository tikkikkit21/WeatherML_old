# Experiment & Dataset Log

## Experiment Log
### Result Overview
| Experiment | Train Acc. | Test Acc. |
| ---------- | ---------- | --------- |
| Exp 1      | 73.47%     | 81.82%    |
| Exp 2      | 79.14%     | 73.68%    |

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

## Dataset Log
**Google Sheets:** https://docs.google.com/spreadsheets/d/1wjoOM3OyRlOUdET7_jU2uoCyOraQOWY8XGOw8LVWK3A

### Version 1
- Added 01/27/2024
- 109 entries

### Version 2
- Added 02/24/2024
- 182 entries
- Added `Gusts` data

### Version 3
- Added 04/06/2024
- 292 Entries
- Removed `Rain?` data
