Welcome to the AWS CodeStar Sample Custom Rule for AWS Config
=============================================================

This sample code helps get you started with a custom rule in AWS Config. The custom rule in this sample
AWS CodeStar project evaluates the Amazon EC2 instances in your AWS account and reports in AWS Config whether each one is of the
instance type as specified in the custom rule (**t2.micro** by default).

For general information about custom rules in AWS Config, see
[Developing Custom Rules for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html)
in the *AWS Config Developer Guide*.

Contents
--------

This sample includes:

* **README.md** - This file.
* **buildspec.yml** - The project pipeline's Build stage uses this file along with the **template.yml** file to deploy the custom rule to AWS Config along with a function
  in AWS Lambda to run the custom rule.
* **rule_code.py** - The custom rule's logic.
* **rule_util.py** - Function code to run the custom rule from AWS Lambda. Do not modify this file.
* **template.yml** - AWS SAM uses this file to instruct AWS CloudFormation how to deploy the custom rule to AWS Config
  along with a function in AWS Lambda to run the custom rule.
* **tests/** - This directory contains unit tests for your application.
* **template-configuration.json** - this file contains the project ARN with placeholders used for tagging resources with the project ID

Getting Started
---------------

Before you can run the custom rule that this project deployed, you must set up Amazon EC2 and AWS Config as follows:

1. If you are using AWS Config in your AWS account for the first time, you must set up AWS Config. Otherwise, the custom rule will not
   run. For instructions, see
   [Setting up AWS Config with the Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html) in the *AWS Config Developer Guide*.
   When following these instructions, make sure to choose the same AWS Region as the AWS CodeStar project. If you have problems accessing the AWS Config
   console, see [Permissions for Accessing AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/recommended-iam-permissions-using-aws-config-console-cli.html)
   in the *AWS Config Developer Guide*.
2. If you do not already have at least one Amazon EC2 instance of type **t2.micro** in your AWS account in the same AWS Region
   as the project, create it. Otherwise, AWS Config will report all of the instances in that AWS Region as **Noncompliant**.
   For instructions, see [Launching an Instance Using the Launch Instance Wizard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launching-instance.html)
   in the *Amazon EC2 User Guide for Linux Instances* or
   [Launching an Instance Using the Launch Instance Wizard](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/launching-instance.html)
   in the *Amazon EC2 User Guide for Windows Instances*.

After you set up Amazon EC2 and AWS Config, to run the custom rule that this project deployed, do the following:

1. With the AWS Config console already displayed and set to the same AWS Region as the AWS CodeStar project, choose **Rules**.
2. Choose the custom rule that the AWS CodeStar project created.
3. Choose **Re-evaluate**.
4. Wait for the rule to finish running, and then see the results in the **Resources evaluated** section.

If the custom rule did not finish running successfully, you can try to fix it by doing the following:

1. Open the AWS Lambda function for the custom rule. To do this, in the AWS CodeStar project's **Project** page, choose the **AWS Lambda** link.
2. On the **Monitoring** tab, choose any of the **Jump to Logs** links to view the related logs in AWS CloudWatch Logs.
3. Check for any invocation errors in the logs, and use those errors to fix your custom rule code as needed.
4. Redeploy your AWS Lambda function. To do this, follow the instructions in the *Next Steps* section to push your code change to the AWS CodeStar project's repository.
5. Go back to the AWS Config console for the rule and choose **Re-evaluate** again.

Next Steps
----------

To change the sample's code, clone the AWS CodeStar project's repository to your local computer manually, or use an IDE that AWS CodeStar supports. For instructions, choose
the **Connect tools** button in your AWS CodeStar project's **Dashboard** or **Project** pages, and then follow the on-screen instructions. Or see
[Use an IDE with AWS CodeStar](https://docs.aws.amazon.com/codestar/latest/userguide/setting-up-ide.html) in the
*AWS CodeStar User Guide*. After you clone the repository, make a code change, and then push the change to the repository.

We suggest making a small code change first, so you can see how changes pushed to your AWS CodeStar project's repository
are automatically picked up by your project's pipeline and then deployed to AWS Config and AWS Lambda.
You can watch the pipeline's progress in the **Continuous deployment** tile on your AWS CodeStar project's **Dashboard** page.
For example, you can change the value of **desiredInstanceType** in the **template.yml** file to a different Amazon EC2 instance type.

To run your tests locally, go to the root directory of the sample code and execute run the `pip install -r requirements.txt`
command to install dependencies required for testing.  Then run the `python -m unittest discover tests` command,
which AWS CodeBuild also runs through your `buildspec.yml` file.

To test your new code during the release process, modify the existing tests or add tests to the tests directory.
AWS CodeBuild will run the tests during the build stage of your project pipeline. You can find the test results
in the AWS CodeBuild console.

Additional Resources
--------------------

* [Evaluating Resources With AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) in the *AWS Config Developer Guide*
* [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
* [AWS Serverless Application Model](https://github.com/awslabs/serverless-application-model/blob/master/HOWTO.md)
* [AWS CodeBuild User Guide](https://docs.aws.amazon.com/codebuild/latest/userguide/concepts.html)
* [User Guide](https://docs.aws.amazon.com/codestar/latest/userguide/welcome.html)
* [Forum](https://forums.aws.amazon.com/forum.jspa?forumID=248)

What Should I Do Before Running My Project in Production?
------------------

AWS recommends you review the security best practices recommended by the framework
author of your selected sample application before running it in production. You
should also regularly review and apply any available patches or associated security
advisories for dependencies used within your application.

* [Best Practices](https://docs.aws.amazon.com/codestar/latest/userguide/best-practices.html?icmpid=docs_acs_rm_sec)
