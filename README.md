# Send Daily Quotes over Instagram Messages

This script uses [Meta Developer APIs](https://developers.facebook.com) to send daily quotes from user's Instagram account to receipient's Instagram account. The quotes are generated through [Quotable APIs](https://github.com/lukePeavey/quotable). The script is invoked daily using [AWS Lambda](https://aws.amazon.com/lambda) and [AWS CloudWatch](https://aws.amazon.com/cloudwatch). Lastly, [AWS API Gateway](https://aws.amazon.com/api-gateway) used during setup.


## Shortcuts

- [Requirements](#requirements)
- [Setup](#setup)
- [References](#references)

## Requirements
* __Recipient's Permission:__ Well obviously don't be a creep and ask the recipient if they are okay with receiving random quotes everyday. This is not only needed for ethical reasons but also needed because you will add their account as "Instagram Tester" to your app. Then, when it's neceessary, they will need to message your account.
* __Instagram Professional Account:__ It sounds pretty serious and scary but don't worry it is free and to be honest it really doesn't have any difference on how your profile looks like from outside. You can either create a Business account or Creater account (if you have <500k followers).
* __Facebook Page:__ You should create a page on Facebook if you don't have one already. It doesn't need to have anything on it but you have to connect your Facebook Page to your Professional Instagram Account.
* __AWS Account:__ Free Tier Account is more than enough for the purpose of this project.
## Setup

## References