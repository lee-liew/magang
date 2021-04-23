#-*- coding: utf-8 -*-

# rf params
rf_params = {
    'n_estimators': 1000,
    'max_depth': 10,
    'max_features': 0.8,
    'min_samples_split': 2,
    'min_samples_leaf': 2,
    'oob_score': True,
    'n_jobs': -1,
    'random_state': 2019
}
<<<<<<< HEAD
=======
rf_grid={'n_estimators':[500,1000,1500],
             'max_depth': [5, 8, 10, 15],
             'max_features': [0.80, 0.90, 0.95],
             'min_samples_split':[2, 5, 8],
             'min_samples_leaf': [1, 3, 5]
}
>>>>>>> 17128e6dc8cc2edbec7a41b9fdde808bd1440031

# xgb params
xgb_params = {
    'objective': 'reg:linear',
    'booster': 'gbtree',
    'learning_rate': 0.01,
    'max_depth': 8,
    'eval_metric': 'rmse',
    'silent': 1,
    'n_jobs': -1,
    'lambda': 1.0,
    'gamma': 0.7,
    'subsample': 0.9,
    'colsample_bytree': 0.9,
    'min_child_weight': 8,
    'n_estimators': 1000,
    'random_state': 2019
}
<<<<<<< HEAD

=======
xgb_grid = {'max_depth': [5, 10, 15],
 'learning_rate': [0.01, 0.02, 0.05],
 'n_estimators': [500, 1000, 2000],
 'min_child_weight': [0, 2, 5],
 'max_delta_step': [0, 0.2, 0.6],
 'subsample': [0.6, 0.7, 0.8],
 'colsample_bytree': [0.5, 0.6, 0.7],
 'reg_alpha': [0, 0.25, 0.5],
 'reg_lambda': [0.2, 0.4, 0.6],
 'scale_pos_weight': [0.2, 0.4, 0.6]
}
>>>>>>> 17128e6dc8cc2edbec7a41b9fdde808bd1440031
# # lgb params
# lgbm_params = {
#     'num_leaves': 70,
#     'seed': 2019,
#     'learning_rate': 0.05,
#     'metric': 'l2_root',
#     'n_estimators': 1000,
#     'n_jobs': -1,
#     'colsample_bytree': 0.8,
#     'max_bin': 511,
#     'reg_alpha': 0.8,
#     'reg_lambda': 1,
#     'subsample': 0.7
# }

# new lgb params
<<<<<<< HEAD
lgbm_params = {
=======
lgbm_params ={
>>>>>>> 17128e6dc8cc2edbec7a41b9fdde808bd1440031
    'num_leaves': 179,
    'seed': 2019,
    'learning_rate': 0.01,
    'metric': 'l2_root',
    'n_estimators': 1000,
<<<<<<< HEAD
    'n_jobs': -1,
=======
    'n_jobs': 32,
>>>>>>> 17128e6dc8cc2edbec7a41b9fdde808bd1440031
    'colsample_bytree': 0.8,
    'max_bin': 680,
    'reg_alpha': 12.99,
    'reg_lambda': 33,
    'min_split_gain': 0,
    'subsample': 0.7
}
<<<<<<< HEAD

=======
#{    'boosting_type': 'gbdt', 
#    'objective': 'regression', 
#    'learning_rate': 0.01, 
#    'num_leaves': 50, 
#    'max_depth': 10,    
#    'subsample': 0.8, 
#    'colsample_bytree': 0.8, 
#    }

lgbm_grid= {'n_estimators': [500, 600],
            'num_leaves':[15,20],
              'max_depth': [5, 6],
              'learning_rate': [0.01, 0.02],
              'feature_fraction': [0.6, 0.7],
              'bagging_fraction': [0.6, 0.7],
              'bagging_freq': [2, 4],
              'lambda_l1': [0, 0.1],
              'lambda_l2': [0, 0.1],
              'cat_smooth': [1, 10]
              }
>>>>>>> 17128e6dc8cc2edbec7a41b9fdde808bd1440031
# extra_tree params
et_params = {
    'n_jobs': -1,
    'random_state': 2019,
    'max_depth': 10,
    'min_samples_leaf': 1,
    'min_samples_split': 2,
    'max_features': 0.95,
    'n_estimators': 1000,
    'criterion': 'mse'
}
<<<<<<< HEAD
=======
et_grid= {'n_estimators':[100,200,500],
             'max_depth': [5, 8, 10, 15],
             'max_features': [0.80, 0.90, 0.95],
             'min_samples_split':[2, 5, 8],
             'min_samples_leaf': [1, 3, 5]
}
>>>>>>> 17128e6dc8cc2edbec7a41b9fdde808bd1440031

# SVR params
svr_params = {'C': 0.1, 'epsilon': 0.01, 'kernel': 'rbf'}

# ANN params
ann_params = {
    'learning_rate': 'adaptive',
    'hidden_layer_sizes': (
        100,
        200,
        300,
        200,
        100,
        50,
        20,
        10,
    ),
    'batch_size': 512,
    'max_iter': 5000,
    'tol': 0.0000000001,
    'random_state': 2018,
    'verbose': True
}
#####CatBoost
cat_params={'iterations':200, 
 'learning_rate':0.03,
        'depth':6, 
 'l2_leaf_reg':3,
        'loss_function':'MAE',
        'eval_metric':'MAE'
             }
<<<<<<< HEAD
=======
cat_grid= {'depth': [4, 7, 10],
          'learning_rate' : [0.03, 0.1, 0.15],
         'l2_leaf_reg': [1,4,9],
         #'task_type':['GPU'],
         'iterations': [300]
             }
>>>>>>> 17128e6dc8cc2edbec7a41b9fdde808bd1440031
