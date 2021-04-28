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
lgbm_params = {
    'num_leaves': 179,
    'seed': 2019,
    'learning_rate': 0.01,
    'metric': 'l2_root',
    'n_estimators': 1000,
    'n_jobs': -1,
    'colsample_bytree': 0.8,
    'max_bin': 680,
    'reg_alpha': 12.99,
    'reg_lambda': 33,
    'min_split_gain': 0,
    'subsample': 0.7
}

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
