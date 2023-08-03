# Instruction

### Commands
To excute Individual Tests for GitHub API tests set environmental value GITHUB_TOKEN such as: 
```
export GITHUB_TOKEN=__your token here__
```

To run the mandatory GitHub API tests use:
```
pytest -m api
```

To run Individual GitHub API tests use:
```
pytest -m api_my
```

To run the mandatory Tests for database use:
```
pytest -m database
```

To run Individual Tests for database use:
```
pytest -m database_my
```

To run the mandatory Tests for GitHub UI use:
```
pytest -m ui
```

To run the Individual Tests for GitHub UI use:
```
pytest -m ui_rztk
```