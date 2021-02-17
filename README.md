<a href="https://www.hengjiu.jp">
    <img src="https://www.hengjiu.jp/img/retina/header_logo@2x.jpg" alt="hengjiu logo" title="hengjiu" align="right" height="50" />
</a>

# AWS-Lambda-CustomNotification

## ランタイム設定情報
- ランタイム：Python 3.8
- ハンドラ：lambda_function.lambda_handler

## 環境変数
| キー              | 値 |
|------------------|------------|
| `CUSTOM_SUBJECT` | SNS Subject |
| `SNS_TOPIC_ARN`  | SNS ARN    |


## 導入
### IAM
- Create Role

```bash:create-role
$ aws iam create-role --role-name CustomNotification --assume-role-policy-document file://trust-policy.json
```

- Attache Role

```bash:attach-role
$ aws iam attach-role-policy --role-name CustomNotification --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

```bash:attach-role
$ aws iam attach-role-policy --role-name CustomNotification --policy-arn arn:aws:iam::aws:policy/AmazonSNSFullAccess
```

### Lambda

- Zip

```bash:zip
$ zip customNotification.zip customNotification.py 
```

- Create Function

```bash:create-function
$ aws lambda create-function --function-name customNotification --role < IAM Role ARN > --runtime python3.8 --handler customNotification.lambda_handler --zip-file fileb://customNotification.zip
```

- Update Function

```bash:update-function
$ aws lambda update-function-configuration --function-name customNotification --environment Variables='{SNS_TOPIC_ARN="< SNS ARN >",CUSTOM_SUBJECT="通知タイトル"}'
```

---

###### 参考URL
- [AWS Lambda 環境変数の使用](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/configuration-envvars.html)
