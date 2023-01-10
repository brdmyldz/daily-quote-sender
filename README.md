
# Send Daily Quotes over Instagram Messages

This script uses [Meta Developer APIs](https://developers.facebook.com) to send daily quotes from user's Instagram account to receipient's Instagram account. The quotes are generated through [Quotable APIs](https://github.com/lukePeavey/quotable). The script is invoked daily using [AWS Lambda](https://aws.amazon.com/lambda) and [AWS CloudWatch](https://aws.amazon.com/cloudwatch). Lastly, [AWS API Gateway](https://aws.amazon.com/api-gateway) used during setup.


## Shortcuts

- [Requirements](#requirements)
- [Setup](#setup)
- [References](#references)
- [Future Improvement Ideas](#future-improvement-ideas)

## Requirements
* ___Recipient's Permission:___ Well obviously go and ask the recipient if they are okay with receiving random quotes everyday. This is not only needed for ethical reasons but also needed because you will add their account as "Instagram Tester" to your app. Then, when it's neceessary, they will need to message your account.
* __Instagram Professional Account:__ It sounds pretty serious and scary but don't worry it is free and to be honest it really doesn't have any difference on how your profile looks like from outside. You can either create a Business account or Creater account (if you have <500k followers).
* __Facebook Page:__ You should create a page on Facebook if you don't have one already. It doesn't need to have anything on it but you have to connect your Facebook Page to your Professional Instagram Account.
* __AWS Account:__ Free Tier Account is more than enough for the purpose of this project.
## Setup

Let's start! I'm assuming you already set your instagram account to professional, and connected your Facebook Page to your instagram account.

1. Open your Meta Developer Account and create a new app. Make sure the app type is "None". ![Select type](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/select-type.png?raw=true)
2. We are going to add the recipient's Instagram account as "Instagram Tester" to our app. First we need to go to Settings->Basic and add a new platform(at the very bottom). You can select "Website" as the platform. If you have a website you can paste the URL of your website here. If you don't you can just paste your github profile URL.
3. Go to the dashboard and click "Set up" on "Instagram Basic Display". ![Set up Instagram Basic Display](https://scontent-sea1-1.xx.fbcdn.net/v/t39.2365-6/116839963_305560353979471_93042950445637590_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ad8a9d&_nc_ohc=IC2XE3yB7LMAX97bfs0&_nc_ht=scontent-sea1-1.xx&oh=00_AfC8rUzSrv-IhhUNYwWC9qLYVsqhyXWHhOAW6DWw0PBfnQ&oe=63C170A7)
4. Go to Instagram Basic Display-> Basic Display and then click "Create New App".
5. Now, if you go to App Roles->Roles, you will see a new section appeared and it's called "Instagram Testers". Go ahead an add your recipient as an Instagram Tester. They will need to accept your invitation.
6. Go to Tools -> Graph API Explorer. Add following permissions:
    1. instagram_basic
    2. instagram_manage_messages
    3. pages_manage_metadata
7. Go ahead and click "Generate Access Token". Don't worry if you get the below error message. ![Log-in error](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/log-in-error.png?raw=true)
8. Copy your Access Code. Now open setup/defines.py and paste your access code in `creds["access_token"]`.
9. Go to the dashboard in Meta and click Settings->Basic. Copy "App ID" and "App Secret" and paste it to `creds["app_id"]` and `creds["app_secret"]`.
10. Note that our access token expires in hours so we need to generate our "Long-Lived Access Token". To do that, run get_long_lives_access_token.py. Copy the long-lived access token from commend line and replace your old access code with the new one(`creds["access_token"]`) in defines.py. This new access code will expire in 90 days.
11. Run get_page_id.py. Copy and paste your Page ID to `creds["page_id"]` in defines.py.
12. Run get_page_access_token.py. Copy and paste your Page Access Token to `creds["page_access_token"]` in defines.py.
13. The only thing left is `creds["recipient_instagram_account_id"]` but this is the hard part.
## Future Improvement Ideas

* get_long_lived_access_token.py, get_page_Acess_token.py, get_page_id.py can be put in one file to make setup process simplier.
## References