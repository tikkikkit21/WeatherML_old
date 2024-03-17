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
