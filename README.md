# Send Daily Quotes over Instagram Messages

This script uses [Meta Developer APIs](https://developers.facebook.com) to send daily quotes from user's Instagram account to receipient's Instagram account. The quotes are generated through [Quotable APIs](https://github.com/lukePeavey/quotable). The script is invoked daily using [AWS Lambda](https://aws.amazon.com/lambda), [AWS CloudWatch](https://aws.amazon.com/cloudwatch) and [AWS EventBridge](https://aws.amazon.com/eventbridge). Lastly, [AWS API Gateway](https://aws.amazon.com/api-gateway) used during setup.
## Shortcuts

- [Requirements](#requirements)
- [Setup](#setup)
- [Future Improvement Ideas](#future-improvement-ideas)
- [References](#references)


## Requirements
* ___Recipient's Permission:___ Well obviously go and ask the recipient if they are okay with receiving random quotes everyday. This is not only needed for ethical reasons but also needed because you will add their account as "Instagram Tester" to your app. Then, when it's neceessary, they will need to message your account.
* __Instagram Professional Account:__ It sounds pretty serious and scary but don't worry it is free and to be honest it really doesn't have any differences on how your profile looks like from outside. You can either create a Business account or Creater account (if you have <500k followers).
* __Facebook Page:__ You should create a page on Facebook if you don't have one already. It doesn't need to have anything on it but you have to connect your Facebook Page to your Professional Instagram Account.
* __AWS Account:__ Free Tier Account is more than enough for the purpose of this project.
## Setup

Let's start! I'm assuming you already set your instagram account to professional, connected your Facebook Page to your instagram account, and cloned the repo in to your local device.

1. Open your Meta Developer Account and create a new app. Make sure the app type is "None". ![select-type](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/select-type.png?raw=true)
2. We are going to add the recipient's Instagram account as "Instagram Tester" to our app. First we need to go to Settings->Basic and add a new platform(at the very bottom). You can select "Website" as the platform. If you have a website you can paste the URL of your website here. If you don't you can just paste your github profile URL.
3. Go to the dashboard and click "Set up" on "Instagram Basic Display". ![Set up Instagram Basic Display](https://scontent-sea1-1.xx.fbcdn.net/v/t39.2365-6/116839963_305560353979471_93042950445637590_n.png?_nc_cat=100&ccb=1-7&_nc_sid=ad8a9d&_nc_ohc=IC2XE3yB7LMAX97bfs0&_nc_ht=scontent-sea1-1.xx&oh=00_AfC8rUzSrv-IhhUNYwWC9qLYVsqhyXWHhOAW6DWw0PBfnQ&oe=63C170A7)
4. Go to Instagram Basic Display-> Basic Display and then click "Create New App".
5. Now, if you go to App Roles->Roles, you will see a new section appeared and it's called "Instagram Testers". Go ahead an add your recipient as an Instagram Tester. They will need to accept your invitation.
6. Go to Tools -> Graph API Explorer. Add following permissions:
    1. instagram_basic
    2. instagram_manage_messages
    3. pages_manage_metadata
7. Go ahead and click "Generate Access Token". Don't worry if you get the below error message. ![login-error](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/log-in-error.png?raw=true)
8. Copy your Access Code. Now open setup/defines.py and paste your access code in `creds["access_token"]`.
9. Go to the dashboard in Meta and click Settings->Basic. Copy "App ID" and "App Secret" and paste it to `creds["app_id"]` and `creds["app_secret"]`.
10. Note that our access token expires in hours so we need to generate our "Long-Lived Access Token". To do that, run get_long_lives_access_token.py. Copy the long-lived access token from commend line and replace your old access code with the new one(`creds["access_token"]`) in defines.py. This new access code will expire in 90 days.
11. Run get_page_id.py. Copy and paste your Page ID to `creds["page_id"]` in defines.py.
12. Run get_page_access_token.py. Copy and paste your Page Access Token to `creds["page_access_token"]` in defines.py.
13. The only thing left is `creds["recipient_instagram_account_id"]` but this is the hard part. To be able to use the messaging API that Instagram provided, recipient needs to send us a message. Then we will catch their message notification via Webhook. This way we can find recipient's sender ID. This ID is specific for the recipient and your Instagram account. More information can be found [here](https://developers.facebook.com/docs/messenger-platform/overview) (under the Instagram-Scoped IDs Section).
14. Go to AWS Lambda and create a new function named api_handler_meta_dev. You can pick the Python's latest version available as a runtime and x86_64 as your Architecture.![create-lambda](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/create-lambda.png?raw=true)
15. Now copy all the code from aws_lambda/verify_token_meta_dev/lambda_function.py. Paste into AWS Lambda and then click "Deploy". After that, click Add trigger and pick "API Gateway" from the drop down list. Choose "Create a new API" and "REST API". Security is up to you but I picked "Open".![add-trigger](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/add-trigger.png?raw=true)
16. Make sure you save your API endpoint to somehwere as we are going to use this endpoint in next steps.![get-endpoint](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/create-lambda.png?raw=true)
17. Let's go back to Meta Dashboard and add "Webhooks" product to our app. Go to Webhooks settings, select "Instagram" from drop down menu and click "Subscribe to this object". Now paste your AWS API endpoint to here and write "12345" to the "Verify token" input.![verify-webhook](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/verify-webhook.png?raw=true)
18. Now that we verify our endpoint go back to our AWS Lambda function. Copy everything from aws_lambda/api_handler_meta_dev/lambda_function.py and paste it there and click "Deploy". Now we are ready to receive requests from Meta.![paste-code](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/paste-code.png?raw=true)
19. Go back to Webhooks settings and subscribe "messages". Now I want you to go back to Meta Dashboard and add "Messenger" product to your app. Go to Messenger->Instagram Settings. Under the Webhooks section click "Subscribe".![subscribe-webhook](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/subscribe-webhook.png?raw=true)
20. Now we can go ahead and let the recipient know that they should send us a message. 
21. After you receive the message on Instagram, go to AWS Lambda screen and click Monitor->View CloudWatch logs.![open-cloudwatch](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/open-cloudwatch.png?raw=true)
22. Here you can see the logs of your API handler. I want you to open the most recent Log stream. ![recent-log](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/recent-log.png?raw=true)
23. In the messages section section you will see the Instagram ID of sender that is unique between your account and the recipient's account. Copy it! ![log-info](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/log-info.png?raw=true)
24. We now have every data we need to call Instagram Message API. Go to setup/defines.py and paste sender's id to `creds["recipient_instagram_account_id"]`. After that if you run setup/send_instagram_message.py, it should send the message "Hello World!" to the recipient.
25. Go to AWS Lambda and create a new function called daily_quote_sender. Copy everything from aws_lambda/daily_quote_sender/lambda_function.py and paste into AWS Lambda. Now copy your Page ID, Page Access Token, Sender Instagram ID from setup/defines.py and paste it into `params["page_id"]`, `params["page_access_token"]`, `params["recipient_instagram_account_id"]` in order in your Lambda function.
26. We want to create a new file in our AWS Function and call it "pull_quote.py". After that copy everything from aws_lambda/daily_quote_sender/pull_quote.py to AWS Lambda. ![pull-quote](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/pull-quote.png?raw=true)
27. AWS Lambda doesn't have every library already installed in it. Thus, we need to import requests library manually. To do that click on "Layers" on the left side menu. ![layer-button](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/layer-button.png?raw=true)
28. Click "Create Layer". Give the name "request-library" to your layer. Upload layer.zip file located in aws_lambda/daily_quote_sender. Pick the same Python version and x86_64 architecture.
29. Come back to your AWS Lambda function and on the very bottom you will see the "Layers" section. From there click on "Add a Layer". You will have to pick "Custom layers" for the source then you can see "requests-library" layer. ![add-layer](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/add-layer.png?raw=true)
30. Don't forget to click "Deploy" in your AWS Lambda function after all these changes.
31. Now the only thing left is setting a scheduler to call our Lambda function daily. For that we will use AWS EventBridge. Go to AWS EventBridge and click on "EventBridge Schedule". After that press on "Create Schedule".
32. Name your schedule "daily_quote_sender". Click "Recurring Schedule". You will have to enter your preferred cron-based expression. Simply google "cron expression generator" and set your settings according to your preference. Set "flexible time window" "Off". Set your "Timezone". ![schedule-settings](https://github.com/brdmyldz/daily-quote-sender/blob/main/images/schedule-settings.png?raw=true)
33. When you come to "Select Target" page, select AWS Lambda and find your fucnction name and select it. You can set other settings if you would like.
34. Lastly, go to your Webhooks settings on Meta Dashboard and unsubscribe from "messages" as we don't want Meta to send our endpoint anymore requests.
35. We are done! Happy coding :)
## Future Improvement Ideas

* get_long_lived_access_token.py, get_page_Acess_token.py, get_page_id.py can be put in one file to make setup process simplier.
* I found out that there is no video on Youtube showing how to setup Messaging API for Instagram. In my free time I want to prepare a video tutorial for this project and upload it to Youtube. 
## References

* [Quotable](https://github.com/lukePeavey/quotable) on Github takes all the credit for the quotes and well set APIs.

* [@justinstolpe](https://www.youtube.com/@justinstolpe) on Youtube was a good resource for this project.