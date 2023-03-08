# Community Engagement

## Scripts
### Update spreadsheet metrics
To update a Github metrics spreadhsheet on Google Drive you should pass as environment a SH_URL variable with the url of the spreadhsheet, GH_TOKEN as the Github Developer token and some Google Developer variables (PRIVATE_KEY, CLIENT_EMAIL and PRIVATE_KEY).

To generate the Github Developer token you can follow this [tutorial](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

To get the necessary Google Developer variables follow this [tutorial](https://docs.gspread.org/en/latest/oauth2.html).

With all this variable at hand you can add each environment variable a secret on your Github repository. To make this follow this [tutorial](https://docs.github.com/en/actions/security-guides/encrypted-secrets).

Remember to also update on code the list of repositories and worksheet names so the script can correctly stipulate information on spreadsheet.


