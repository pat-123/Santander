This is a classification problem, to predict if a customer will make a transaction in future or not

Few points worth mentioning regarding directory structure:
--train and test dataset is placed under data/raw/
--Processed data is placed under data/processed after computation
--Test predictions are available under data/submitted
--Notebook is present in notebooks folder
--Santander is a package which load all initial packages(__init__.py) and sets data file paths under config.py
  ++ Abstracts the messy paths in the main notebook to here, so that cleaner view can be provided
--scripts folder is a placeholder for future purposes

-- Demonstrated model results with train_test_splits and also KFolds 

-- write a OOPS style framework for running different ML regressor algo on the cleaned data and compare performance and choose the best ML model suited for this model

---------------------------------------------------
How to run this?
-----------------------------------------------------
  ++ start Anaconda prompt and go to this folder's parent location and type jupyter notebook or just go inside the folder notebooks in the cur directory and type 'jupyter notebook Santander' on anaconda prompt.
  ++ FYI- In the first option, notebook starts with the parent folder as the base location and you can navigate to different projects from there

---------------------------------------------------
New additions
--------------------------------------------------
++ Add ROC/AUC in the framework

-------------------------------------------------- 
RESULT
--------------------------------------------------
Data is imbalanced, used SMOTE
RandomForest out performs Logistic Regression and Naive Bayes over 5 KFolds with an accuracy of 93% and auc score of 0.98(round up to 2 decimal places)

------------------------------------------------------
SUMMARY
----------------------------------------------------
This project is about predicting if a customer will do transaction or not in future(irrespective of the amount of transaction)

With the predictions, we are more intrested to find out customers who are likely to make a transaction rather than the people who will not.

-----So basically we are focussing on positive cases the model can identify i.e. the recall(sensitivity) rather than specificity(True negative rate)

-----And it would cost a lot to loose on customers who are likely to make a transaction, i.e. False negative rate should be low(which is labeled as negative but they were actually positive

So our focus is to get a model with high recall and low FNR, rather than specifity and FPR.
and RandomForest performs the best in these areas, preprocessing:
1. Missing values in Test
2. Taking care of skew and kurtosis in columns
3. Outliers removal
4. SMOTE is applied(since imbalanced target variable) 
5.Normalization
6. Then the model

Moreover the auc value is also highest for randomforest(see Santander_Report.docx for details)

If the data is not pre-processes properly, it is observed that naive bayes outperforms the rest.

