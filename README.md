# Send Daily Quotes over Instagram Messages

This script uses [Meta Developer APIs](https://developers.facebook.com) to send daily quotes from user's Instagram account to receipient's Instagram account. The quotes are generated through [Quotable APIs](https://github.com/lukePeavey/quotable). The script is invoked daily using [AWS Lambda](https://aws.amazon.com/lambda) and [AWS CloudWatch](https://aws.amazon.com/cloudwatch). Lastly, [AWS API Gateway](https://aws.amazon.com/api-gateway) used during setup.


## Shortcuts

- [Requirements](#requirements)
- [Setup](#setup)
- [References](#references)

## Requirements
* ___Recipient's Permission:___ Well obviously don't be a creep and ask the recipient if they are okay with receiving random quotes everyday. This is not only needed for ethical reasons but also needed because you will add their account as "Instagram Tester" to your app. Then, when it's neceessary, they will need to message your account.
* ___Instagram Professional Account:___ It sounds pretty serious and scary but don't worry it is free and to be honest it really doesn't have any difference on how your profile looks like from outside. You can either create a Business account or Creater account (if you have <500k followers).
* ___Facebook Page:___ You should create a page on Facebook if you don't have one already. It doesn't need to have anything on it but you have to connect your Facebook Page to your Professional Instagram Account.
* ___AWS Account:___ Free Tier Account is more than enough for the purpose of this project.

## Setup

Let's start! I'm assuming you already set your instagram account to professional, and connected your Facebook Page to your instagram account.

    1. Open your Meta Developer Account and create a new app. Make sure the app type is "None".
    2. Go to Tools -> Graph API Explorer. Add following permissions:
        - instagram_basic
        - instagram_manage_messages
        - pages_manage_metadata
    3. Go ahead and click "Generate Access Token". Don't worry if you get the below error message.
    4. Copy your Access Code. Now open setup/defines.py and paste your access code in `creds["access_token"]`.
    5. Go to the dashboard in Meta and click Settings->Basic. Copy "App ID" and "App Secret" and paste it to `creds["app_id"]` and `creds["app_secret"]`.
    6. Now we are going to add the recipient's Instagram account as "Instagram Tester" to our app. First we need to go to Settings->Basic and at the very bottom we need to add a new platform. You can select "Website" as the platform. If you have a website you can paste the URL of your website here. If you don't you can just paste your github profile URL.
    7. Now go to the dashboard and click "Set up" on Instagram Basic Display.
    ![Set up Instagram Basic Display](https://scontent-sea1-1.xx.fbcdn.net/v/t39.2365-6/116839963_305560353979471_93042950445637590_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ad8a9d&_nc_ohc=IC2XE3yB7LMAX97bfs0&_nc_ht=scontent-sea1-1.xx&oh=00_AfC8rUzSrv-IhhUNYwWC9qLYVsqhyXWHhOAW6DWw0PBfnQ&oe=63C170A7)
    8. 
## References