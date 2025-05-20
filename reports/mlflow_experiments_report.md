# MLflow Tracking Report (All Experiments)

## Experiment: foresight_nn2
- ID: 3
- Artifact Location: mlflow-artifacts:/8aaf25385f3c450f9ba855f7fe2a2dea
- Lifecycle Stage: active

### Run: masked-hog-111
- Run ID: b2b28aa066bd4e45ac6766ba7cae9eca
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-01 17:42:58
- End Time: 2025-05-01 18:36:47
- Duration: 3228.87 seconds
- Parameters:
  - activation_1: relu
  - num_layers: 1
  - lr: 0.001
  - tuner/bracket: 2
  - tuner/trial_id: 0011
  - activation_0: relu
  - units_1: 48
  - tuner/round: 1
  - units_0: 50
  - tuner/initial_epoch: 2
  - optimizer: Adam
  - tuner/epochs: 4
- Metrics:
  - accuracy: 0.681038498878479
  - val_accuracy: 0.34091657400131226
  - loss: 0.7843527793884277
  - val_loss: 1.2088227272033691
  - test_AUC: 0.9247967907758291
- Artifacts:
  - confusion_matrix.jpg
  - model
  - y_comparison_hist.jpg

---

### Run: bustling-boar-363
- Run ID: 350e5ef9d6cc4f7ba965b19e73fba678
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-01 17:12:42
- End Time: 2025-05-01 17:15:23
- Duration: 161.11 seconds
- Parameters:
  - tuner/bracket: 2
  - tuner/epochs: 2
  - activation_0: relu
  - activation_1: relu
  - optimizer: Adagrad
  - num_layers: 2
  - units_0: 26
  - lr: 0.01
  - units_1: 48
  - tuner/initial_epoch: 0
  - tuner/round: 0
- Metrics:
  - accuracy: 0.730045735836029
  - val_accuracy: 0.7654343843460083
  - loss: 0.9005334377288818
  - val_loss: 0.5316635370254517
  - test_AUC: 0.9032572650226628
- Artifacts:
  - confusion_matrix.jpg
  - keras_model
  - y_hist.jpg

---

### Run: welcoming-crab-703
- Run ID: d31d62a8aed24606922eeefbaf6ba5e7
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-01 15:48:10
- End Time: 2025-05-01 16:31:28
- Duration: 2597.80 seconds
- Parameters:
  - optimizer: Adam
  - tuner/trial_id: 0000
  - num_layers: 1
  - units_0: 38
  - activation_0: relu
  - lr: 0.01
  - tuner/epochs: 4
  - tuner/initial_epoch: 2
  - tuner/bracket: 2
  - tuner/round: 1
  - units_1: 36
  - activation_1: leaky_relu
- Metrics:
  - accuracy: 0.6821416020393372
  - val_accuracy: 0.43209102749824524
  - loss: 0.7154052257537842
  - val_loss: 1.648645281791687
  - test_AUC: 0.9087635761892493
- Artifacts:
  - confusion_matrix.jpg
  - keras_model
  - y_hist.jpg

---

### Run: stylish-asp-676
- Run ID: d0c7eef3bef4464c9511a43c365288bf
- User: Jesolis14
- Status: FAILED
- Start Time: 2025-05-01 13:21:07
- End Time: 2025-05-01 13:21:10
- Duration: 3.16 seconds
- Parameters:
  - None
- Metrics:
  - None
- Artifacts:
  - None

---

### Run: charming-mare-925
- Run ID: edc27c559f704aba9c94e84f5f685c99
- User: Jesolis14
- Status: RUNNING
- Start Time: 2025-05-01 11:58:11
- End Time: N/A
- Duration: Unknown
- Parameters:
  - units_1: 24
  - num_layers: 2
  - units_0: 22
  - activation_0: relu
  - optimizer: Adagrad
  - lr: 0.0001
  - activation_1: leaky_relu
  - tuner/epochs: 2
  - tuner/bracket: 2
  - tuner/initial_epoch: 0
  - tuner/round: 0
- Metrics:
  - None
- Artifacts:
  - tensorflow_model

---

## Experiment: foresight_knn
- ID: 2
- Artifact Location: mlflow-artifacts:/d2ed0a9793184fcab31ecd99f756f80f
- Lifecycle Stage: active

### Run: selective-goose-554
- Run ID: 0c8cc7394b2045e2897dbfa97931e5ca
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 16:44:56
- End Time: 2025-05-18 16:52:17
- Duration: 440.95 seconds
- Parameters:
  - algorithm: ball_tree
  - leaf_size: 40
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.27604246139526367
  - std_fit_time: 0.017969118550426235
  - mean_score_time: 0.5462320645650228
  - std_score_time: 0.02543297186089182
  - mean_test_score: 0.6172435784390693
  - std_test_score: 0.0018632981682755294
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: smiling-goose-19
- Run ID: 0ed3e48fc95347f79b5dd7f56622cd2d
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 16:44:56
- End Time: 2025-05-18 16:52:17
- Duration: 440.95 seconds
- Parameters:
  - algorithm: auto
  - leaf_size: 20
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 2
  - weights: distance
- Metrics:
  - mean_fit_time: 0.40848501523335773
  - std_fit_time: 0.03310756292975106
  - mean_score_time: 0.7296857039133707
  - std_score_time: 0.07564880467018097
  - mean_test_score: 0.6172435784390693
  - std_test_score: 0.0018632981682755294
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: delicate-penguin-585
- Run ID: 737ce3a1eb16454fb5cdb578bcb69584
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 16:44:56
- End Time: 2025-05-18 16:52:17
- Duration: 440.95 seconds
- Parameters:
  - algorithm: ball_tree
  - leaf_size: 50
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 2
  - weights: distance
- Metrics:
  - mean_fit_time: 0.2813904285430908
  - std_fit_time: 0.02389747194936125
  - mean_score_time: 0.5807676315307617
  - std_score_time: 0.06737120928370574
  - mean_test_score: 0.6172435784390693
  - std_test_score: 0.0018632981682755294
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: wise-frog-210
- Run ID: 9fb0c08843c546ad93f499c311736862
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 16:44:56
- End Time: 2025-05-18 16:52:17
- Duration: 440.95 seconds
- Parameters:
  - algorithm: kd_tree
  - leaf_size: 50
  - metric: minkowski
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.37259777386983234
  - std_fit_time: 0.011698455543188376
  - mean_score_time: 0.7638922532399496
  - std_score_time: 0.003065450667601868
  - mean_test_score: 0.6172435784390693
  - std_test_score: 0.0018632981682755294
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: colorful-shad-590
- Run ID: a6b3049121bc40ae85c85b2823028ae3
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 16:44:56
- End Time: 2025-05-18 16:52:17
- Duration: 440.95 seconds
- Parameters:
  - algorithm: kd_tree
  - leaf_size: 40
  - metric: minkowski
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.4000851313273112
  - std_fit_time: 0.025085594550222266
  - mean_score_time: 0.8890215555826823
  - std_score_time: 0.08812311645570581
  - mean_test_score: 0.6172435784390693
  - std_test_score: 0.0018632981682755294
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: capricious-loon-958
- Run ID: d8120f7834704572967d73fea04e1020
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 16:44:56
- End Time: 2025-05-18 16:52:42
- Duration: 465.59 seconds
- Parameters:
  - cv: 3
  - error_score: nan
  - estimator: KNeighborsClassifier()
  - n_iter: 500
  - n_jobs: -1
  - param_distributions: {'n_neighbors': [3, 5, 7, 9, 11, 13], 'weights': ['uniform', 'distance'], 'algorithm': ['auto', 'kd_tree', 'ball_tree'], 'leaf_size': [20, 30, 40, 50], 'p': [1, 2], 'metric': ['euclidean', 'manhattan', 'minkowski']}
  - pre_dispatch: 2*n_jobs
  - random_state: 42
  - refit: True
  - return_train_score: False
  - scoring: f1_macro
  - verbose: 2
  - best_weights: distance
  - best_p: 1
  - best_n_neighbors: 5
  - best_metric: minkowski
  - best_leaf_size: 40
  - best_algorithm: kd_tree
- Metrics:
  - training_precision_score: 1.0
  - training_recall_score: 1.0
  - training_f1_score: 1.0
  - training_accuracy_score: 1.0
  - training_log_loss: 2.2204460492503136e-16
  - training_roc_auc: 1.0
  - training_score: 1.0
  - best_cv_score: 0.6172435784390693
- Artifacts:
  - best_estimator
  - confusion_matrix.jpg
  - cv_results.csv
  - estimator.html
  - knn_model
  - model
  - training_confusion_matrix.png

---

### Run: sincere-goat-673
- Run ID: 0156509b13ea48329391d4ba6002f285
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-15 08:35:22
- End Time: 2025-05-15 08:42:54
- Duration: 452.26 seconds
- Parameters:
  - algorithm: auto
  - leaf_size: 20
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 2
  - weights: distance
- Metrics:
  - mean_fit_time: 0.4395560423533122
  - std_fit_time: 0.025249326529641635
  - mean_score_time: 0.8895472685496012
  - std_score_time: 0.10125209136004472
  - mean_test_score: 0.6170539066069561
  - std_test_score: 0.0007857296727354603
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: kindly-ant-535
- Run ID: 0bfab0034f8346db900f259dd46ed0a3
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-15 08:35:22
- End Time: 2025-05-15 08:43:22
- Duration: 480.00 seconds
- Parameters:
  - cv: 3
  - error_score: nan
  - estimator: KNeighborsClassifier()
  - n_iter: 500
  - n_jobs: -1
  - param_distributions: {'n_neighbors': [3, 5, 7, 9, 11, 13], 'weights': ['uniform', 'distance'], 'algorithm': ['auto', 'kd_tree', 'ball_tree'], 'leaf_size': [20, 30, 40, 50], 'p': [1, 2], 'metric': ['euclidean', 'manhattan', 'minkowski']}
  - pre_dispatch: 2*n_jobs
  - random_state: 42
  - refit: True
  - return_train_score: False
  - scoring: f1_macro
  - verbose: 2
  - best_weights: distance
  - best_p: 1
  - best_n_neighbors: 5
  - best_metric: minkowski
  - best_leaf_size: 40
  - best_algorithm: kd_tree
  - weights: distance
  - p: 1
  - n_neighbors: 5
  - metric: minkowski
  - leaf_size: 40
  - algorithm: kd_tree
- Metrics:
  - accuracy: 0.76085
  - f1_macro: 0.6247539257580152
  - training_precision_score: 1.0
  - training_recall_score: 1.0
  - training_f1_score: 1.0
  - training_accuracy_score: 1.0
  - training_log_loss: 2.2204460492503136e-16
  - training_roc_auc: 1.0
  - training_score: 1.0
  - best_cv_score: 0.6170539066069561
- Artifacts:
  - best_estimator
  - confusion_matrix.jpg
  - cv_results.csv
  - estimator.html
  - knn_model
  - model
  - training_confusion_matrix.png

---

### Run: bedecked-bear-905
- Run ID: 2ad2afcd3db94d4596a6f6e2113a726e
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-15 08:35:22
- End Time: 2025-05-15 08:42:54
- Duration: 452.26 seconds
- Parameters:
  - algorithm: ball_tree
  - leaf_size: 50
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 2
  - weights: distance
- Metrics:
  - mean_fit_time: 0.28076895078023273
  - std_fit_time: 0.018909847429593674
  - mean_score_time: 0.7049736976623535
  - std_score_time: 0.12237039152525286
  - mean_test_score: 0.6170539066069561
  - std_test_score: 0.0007857296727354603
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: rumbling-ape-782
- Run ID: 4ea05c464a0243d3b0b6cb64f551507c
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-15 08:35:22
- End Time: 2025-05-15 08:42:54
- Duration: 452.26 seconds
- Parameters:
  - algorithm: kd_tree
  - leaf_size: 40
  - metric: minkowski
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.4082147280375163
  - std_fit_time: 0.03395587715909787
  - mean_score_time: 0.9950459798177084
  - std_score_time: 0.1260288920639027
  - mean_test_score: 0.6170539066069561
  - std_test_score: 0.0007857296727354603
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: chill-shrimp-64
- Run ID: c3f4a3508f6c40279172873397359145
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-15 08:35:22
- End Time: 2025-05-15 08:42:54
- Duration: 452.26 seconds
- Parameters:
  - algorithm: kd_tree
  - leaf_size: 50
  - metric: minkowski
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.3774302005767822
  - std_fit_time: 0.015664288457028115
  - mean_score_time: 0.8294839859008789
  - std_score_time: 0.06356169504955322
  - mean_test_score: 0.6170539066069561
  - std_test_score: 0.0007857296727354603
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: bustling-turtle-825
- Run ID: eafc618bda9f461aae2dff5e092328ce
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-15 08:35:22
- End Time: 2025-05-15 08:42:54
- Duration: 452.26 seconds
- Parameters:
  - algorithm: ball_tree
  - leaf_size: 40
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.2918357054392497
  - std_fit_time: 0.00851112279497457
  - mean_score_time: 0.8608312606811523
  - std_score_time: 0.17360660247977572
  - mean_test_score: 0.6170539066069561
  - std_test_score: 0.0007857296727354603
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: peaceful-fish-551
- Run ID: 81771b95ad0446a8a571cd5295dd59a7
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-15 08:29:24
- End Time: 2025-05-15 08:36:36
- Duration: 432.31 seconds
- Parameters:
  - weights: distance
  - p: 1
  - n_neighbors: 5
  - metric: minkowski
  - leaf_size: 40
  - algorithm: kd_tree
- Metrics:
  - f1_macro: 0.6277217910959036
  - accuracy: 0.7635
- Artifacts:
  - confusion_matrix.jpg
  - knn_model

---

### Run: resilient-ram-823
- Run ID: 9e2d4c46e9b74967b4eeaad370de3bdc
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-12 17:15:41
- End Time: 2025-05-12 17:22:58
- Duration: 437.31 seconds
- Parameters:
  - weights: distance
  - p: 1
  - n_neighbors: 5
  - metric: minkowski
  - leaf_size: 40
  - algorithm: kd_tree
- Metrics:
  - f1_macro: 0.625364300218888
  - accuracy: 0.7627166666666667
- Artifacts:
  - confusion_matrix.png
  - knn_model

---

### Run: popular-donkey-447
- Run ID: 325e770fbb3c41c6915706922474620a
- User: Jesolis14
- Status: FAILED
- Start Time: 2025-05-12 17:07:41
- End Time: 2025-05-12 17:15:08
- Duration: 446.39 seconds
- Parameters:
  - None
- Metrics:
  - None
- Artifacts:
  - None

---

### Run: stylish-auk-433
- Run ID: 5b22b8fc2c294d7692b581555723428f
- User: Jesolis14
- Status: FAILED
- Start Time: 2025-05-12 17:01:18
- End Time: 2025-05-12 17:05:46
- Duration: 268.39 seconds
- Parameters:
  - None
- Metrics:
  - None
- Artifacts:
  - None

---

### Run: popular-chimp-52
- Run ID: 81245f08600a431fab7b31cef3a61b49
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-12 16:43:44
- End Time: 2025-05-12 16:51:08
- Duration: 444.04 seconds
- Parameters:
  - weights: distance
  - p: 1
  - n_neighbors: 5
  - metric: minkowski
  - leaf_size: 40
  - algorithm: kd_tree
- Metrics:
  - accuracy: 0.7621333333333333
  - f1_macro: 0.6235473650754755
- Artifacts:
  - confusion_matrix.png
  - knn_model

---

### Run: able-dog-995
- Run ID: 4e5639826ad8496aba62f6d168e42d9a
- User: Jesolis14
- Status: FAILED
- Start Time: 2025-05-12 16:32:32
- End Time: 2025-05-12 16:39:44
- Duration: 432.09 seconds
- Parameters:
  - weights: distance
  - p: 1
  - n_neighbors: 5
  - metric: minkowski
  - leaf_size: 40
  - algorithm: kd_tree
- Metrics:
  - f1_macro: 0.625354898457479
  - accuracy: 0.7614333333333333
- Artifacts:
  - None

---

### Run: redolent-bug-135
- Run ID: 482364510ca94dbd8340464acbcec43f
- User: Jesolis14
- Status: RUNNING
- Start Time: 2025-05-01 10:54:05
- End Time: N/A
- Duration: Unknown
- Parameters:
  - None
- Metrics:
  - None
- Artifacts:
  - None

---

### Run: merciful-flea-8
- Run ID: 01845808e2404ad18f8a37755d734091
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-04-30 18:34:18
- End Time: 2025-04-30 18:40:39
- Duration: 380.90 seconds
- Parameters:
  - leaf_size: 20
  - p: 1
  - weights: distance
  - n_neighbors: 3
  - metric: minkowski
  - algorithm: ball_tree
- Metrics:
  - train_accuracy: 1.0
  - val_accuracy: 0.7429
- Artifacts:
  - knn_model
  - matriz.jpg

---

### Run: bustling-snail-151
- Run ID: 143a364c401248e2a12ed7ae7dd1dd41
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-04-30 18:26:53
- End Time: 2025-04-30 18:33:32
- Duration: 398.89 seconds
- Parameters:
  - weights: distance
  - p: 1
  - n_neighbors: 3
  - metric: minkowski
  - leaf_size: 20
  - algorithm: ball_tree
- Metrics:
  - train_accuracy: 1.0
  - val_accuracy: 0.743175
- Artifacts:
  - knn_model
  - matriz.jpg

---

### Run: gifted-shark-178
- Run ID: 226bae99c6304c859b881238a12851e1
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-04-30 18:19:52
- End Time: 2025-04-30 18:26:03
- Duration: 371.08 seconds
- Parameters:
  - weights: distance
  - p: 1
  - n_neighbors: 3
  - metric: minkowski
  - leaf_size: 20
  - algorithm: ball_tree
- Metrics:
  - train_accuracy: 1.0
  - val_accuracy: 0.74125
- Artifacts:
  - knn_model
  - matriz.jpg

---

### Run: carefree-snail-172
- Run ID: 751522460d064ca8a8f7188e48bbb2d2
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-04-30 17:59:30
- End Time: 2025-04-30 18:05:43
- Duration: 373.25 seconds
- Parameters:
  - algorithm: ball_tree
  - weights: distance
  - p: 1
  - n_neighbors: 3
  - metric: minkowski
  - leaf_size: 20
- Metrics:
  - train_accuracy: 1.0
  - val_accuracy: 0.7421083333333334
- Artifacts:
  - knn_model
  - matriz.jpg

---

## Experiment: foresight_nn
- ID: 1
- Artifact Location: mlflow-artifacts:/0305fbfdf7984157974462833acff2e2
- Lifecycle Stage: active

### Run: bald-carp-456
- Run ID: e3e660f7d3c94c2d9faf5d95888cda54
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-12 13:37:26
- End Time: 2025-05-12 13:45:51
- Duration: 504.95 seconds
- Parameters:
  - units_1: 36
  - num_layers: 2
  - tuner/round: 0
  - lr: 0.0001
  - tuner/epochs: 2
  - activation_1: relu
  - activation_0: relu
  - tuner/initial_epoch: 0
  - tuner/bracket: 2
  - optimizer: Adagrad
  - units_0: 26
- Metrics:
  - val_AUC: 0.0
  - accuracy: 0.21503974497318268
  - val_loss: 1.861190915107727
  - loss: 2.0551178455352783
  - AUC: 0.5003027319908142
  - val_accuracy: 0.0
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - matriz.jpg
  - tensorflow_model
  - y_hist.jpg

---

### Run: blushing-sponge-820
- Run ID: 2cf8e51d6a69429bba45947e81ce4854
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-05-03 11:57:18
- End Time: 2025-05-03 11:57:24
- Duration: 5.17 seconds
- Parameters:
  - None
- Metrics:
  - None
- Artifacts:
  - None

---

### Run: omniscient-cod-203
- Run ID: dc7461e63c254f33a822c59f1b73a7a1
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-05-03 11:53:31
- End Time: 2025-05-03 11:53:36
- Duration: 5.38 seconds
- Parameters:
  - None
- Metrics:
  - None
- Artifacts:
  - None

---

### Run: redolent-mouse-820
- Run ID: c860b98a4dea4dafba4d4083f7669e58
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-05-03 11:48:12
- End Time: 2025-05-03 11:48:16
- Duration: 4.93 seconds
- Parameters:
  - None
- Metrics:
  - None
- Artifacts:
  - None

---

### Run: bedecked-rook-724
- Run ID: 3de6caeb029d4c38ac2ae7f0ac0200d0
- User: MaAnCoSa
- Status: RUNNING
- Start Time: 2025-05-03 11:43:47
- End Time: N/A
- Duration: Unknown
- Parameters:
  - None
- Metrics:
  - None
- Artifacts:
  - None

---

### Run: tasteful-lynx-989
- Run ID: e7026e0152a14213a7b380590be1d386
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-29 08:48:23
- End Time: 2025-04-29 08:53:39
- Duration: 316.37 seconds
- Parameters:
  - lr: 0.0001
  - tuner/bracket: 2
  - num_layers: 2
  - tuner/round: 0
  - activation_0: relu
  - activation_1: relu
  - optimizer: Adagrad
  - units_0: 42
  - units_1: 28
  - tuner/initial_epoch: 0
  - tuner/epochs: 2
- Metrics:
  - val_accuracy: 0.0
  - accuracy: 0.21061693131923676
  - AUC: 0.5000926852226257
  - val_AUC: 0.0
  - loss: 2.0780093669891357
  - val_loss: 2.1272919178009033
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - matriz.jpg
  - tensorflow_model
  - y_hist.jpg

---

### Run: useful-slug-294
- Run ID: a0cac210f53d4c6aba52a6f138f0fdae
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-29 07:49:54
- End Time: 2025-04-29 08:21:32
- Duration: 1898.74 seconds
- Parameters:
  - num_layers: 2
  - units_0: 34
  - tuner/epochs: 10
  - tuner/initial_epoch: 0
  - tuner/bracket: 0
  - units_1: 50
  - activation_0: relu
  - lr: 0.0001
  - activation_1: leaky_relu
  - optimizer: Adagrad
  - tuner/round: 0
- Metrics:
  - accuracy: 0.2148977518081665
  - val_accuracy: 1.0825674507941585e-05
  - AUC: 0.49946242570877075
  - val_AUC: 0.0
  - loss: 1.8996390104293823
  - val_loss: 1.8877196311950684
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - matriz.jpg
  - tensorflow_model
  - y_hist.jpg

---

### Run: skillful-fish-232
- Run ID: a055a34dbb014e0e854babf90391a3d5
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-29 07:44:41
- End Time: 2025-04-29 07:47:19
- Duration: 158.33 seconds
- Parameters:
  - units_1: 20
  - units_0: 24
  - activation_0: relu
  - lr: 0.001
  - optimizer: Adagrad
  - num_layers: 2
  - activation_1: relu
- Metrics:
  - AUC: 0.5000489354133606
  - val_accuracy: 0.012955973856151104
  - loss: 1.6426689624786377
  - accuracy: 0.23557323217391968
  - val_loss: 2.1789698600769043
  - val_AUC: 0.0
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - matriz.jpg
  - tensorflow_model
  - y_hist.jpg

---

### Run: mysterious-owl-353
- Run ID: c4fae9e29dab4f9aace1f1474f6eebac
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-04-29 07:40:44
- End Time: 2025-04-29 07:43:21
- Duration: 157.60 seconds
- Parameters:
  - num_layers: 1
  - activation_0: leaky_relu
  - activation_1: leaky_relu
  - units_1: 50
  - units_0: 48
  - optimizer: Adagrad
  - lr: 0.0001
- Metrics:
  - accuracy: 0.23939484357833862
  - val_accuracy: 0.11578719317913055
  - AUC: 0.5015129446983337
  - val_loss: 1.6895495653152466
  - val_AUC: 0.0
  - loss: 1.9178879261016846
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - tensorflow_model

---

### Run: capricious-asp-592
- Run ID: d7ed3cc9f37b4ed78dbd7cf4b87bb246
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-04-29 07:34:40
- End Time: 2025-04-29 07:37:13
- Duration: 153.17 seconds
- Parameters:
  - activation_0: leaky_relu
  - units_0: 30
  - lr: 0.001
  - optimizer: Adam
  - num_layers: 1
- Metrics:
  - val_accuracy: 0.27993741631507874
  - accuracy: 0.5449344515800476
  - AUC: 0.6313230991363525
  - val_loss: 1.4521578550338745
  - val_AUC: 0.0
  - loss: 1.06886887550354
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - tensorflow_model

---

### Run: salty-worm-899
- Run ID: 539eaff9f6564882bb1bc7a223b9152a
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-04-29 07:20:33
- End Time: 2025-04-29 07:20:35
- Duration: 2.42 seconds
- Parameters:
  - None
- Metrics:
  - None
- Artifacts:
  - None

---

### Run: valuable-penguin-216
- Run ID: 7a5c5142347c41f8be99a81640957adc
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-04-29 07:12:41
- End Time: 2025-04-29 07:12:44
- Duration: 2.69 seconds
- Parameters:
  - None
- Metrics:
  - None
- Artifacts:
  - None

---

### Run: valuable-gnat-861
- Run ID: 68ac7550e5174bdfbc20073bdfe42887
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-29 07:00:22
- End Time: 2025-04-29 07:02:38
- Duration: 136.20 seconds
- Parameters:
  - activation_0: relu
  - optimizer: Adagrad
  - lr: 0.001
  - units_0: 40
  - num_layers: 1
- Metrics:
  - val_AUC: 0.0
  - accuracy: 0.5234473943710327
  - loss: 1.4972013235092163
  - val_accuracy: 0.2838684618473053
  - AUC: 0.5932797193527222
  - val_loss: 4.847224235534668
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - matriz.jpg
  - tensorflow_model
  - y_hist.jpg

---

### Run: nimble-kit-814
- Run ID: 8198f38573f3495aac9fb25ad82f4dad
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-29 06:47:54
- End Time: 2025-04-29 06:50:17
- Duration: 142.80 seconds
- Parameters:
  - num_layers: 1
  - units_0: 48
  - activation_0: relu
  - units_1: 34
  - optimizer: Adagrad
  - activation_1: relu
  - lr: 0.0001
- Metrics:
  - val_loss: 2.1793875694274902
  - accuracy: 0.470475435256958
  - val_accuracy: 0.21923409402370453
  - AUC: 0.6211978793144226
  - val_AUC: 0.0
  - loss: 1.3048189878463745
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - matriz.jpg
  - tensorflow_model
  - y_hist.jpg

---

### Run: salty-duck-926
- Run ID: 2bb291751b854c31a71eb3e9721c6295
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-29 06:43:59
- End Time: 2025-04-29 06:44:38
- Duration: 39.15 seconds
- Parameters:
  - activation_1: relu
  - units_1: 36
  - optimizer: Adagrad
  - lr: 0.0001
  - units_0: 22
  - activation_0: relu
  - num_layers: 2
- Metrics:
  - accuracy: 0.3054700195789337
  - val_accuracy: 0.0
  - AUC: 0.49980440735816956
  - val_AUC: 0.0
  - loss: 1774.1883544921875
  - val_loss: 145.90423583984375
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - matriz.jpg
  - tensorflow_model
  - y_hist.jpg

---

### Run: victorious-rook-593
- Run ID: 71208c0c826545a0a124df18c7156248
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-04-29 06:39:20
- End Time: 2025-04-29 06:39:57
- Duration: 36.64 seconds
- Parameters:
  - optimizer: Adam
  - units_0: 20
  - num_layers: 1
  - lr: 0.01
  - activation_0: leaky_relu
- Metrics:
  - val_AUC: 0.0
  - loss: 3.504988193511963
  - val_loss: 478.02362060546875
  - accuracy: 0.45828068256378174
  - AUC: 0.5590900182723999
  - val_accuracy: 0.0012634852901101112
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - tensorflow_model

---

### Run: bedecked-asp-681
- Run ID: 6ff758d8bdb943439e92d48443a412aa
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-04-29 06:37:22
- End Time: 2025-04-29 06:37:59
- Duration: 36.63 seconds
- Parameters:
  - optimizer: Adagrad
  - num_layers: 2
  - units_0: 36
  - units_1: 22
  - lr: 0.001
  - activation_1: leaky_relu
  - activation_0: relu
- Metrics:
  - AUC: 0.5225732922554016
  - val_accuracy: 0.0
  - val_AUC: 0.0
  - val_loss: 15574.88671875
  - loss: 5.165268898010254
  - accuracy: 0.3320184051990509
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - tensorflow_model

---

### Run: resilient-stork-658
- Run ID: b0ed4c77bbb44fa087abaddd5cfc7466
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-28 23:50:20
- End Time: 2025-04-28 23:54:16
- Duration: 235.39 seconds
- Parameters:
  - lr: 0.0001
  - tuner/round: 0
  - num_layers: 2
  - optimizer: Adagrad
  - tuner/epochs: 2
  - activation_0: relu
  - units_1: 20
  - units_0: 32
  - activation_1: leaky_relu
  - tuner/initial_epoch: 0
  - tuner/bracket: 2
- Metrics:
  - val_loss: 10.68796443939209
  - loss: 1.583595871925354
  - val_accuracy: 0.0
  - val_AUC: 0.0
  - accuracy: 0.304941862821579
  - AUC: 0.5001883506774902
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - tensorflow_model

---

### Run: worried-asp-442
- Run ID: 514c934d711541149f457ae3e0bbd4db
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-28 22:41:30
- End Time: 2025-04-28 23:08:47
- Duration: 1636.72 seconds
- Parameters:
  - lr: 0.0001
  - tuner/trial_id: 0006
  - tuner/bracket: 2
  - units_0: 30
  - num_layers: 2
  - optimizer: Adam
  - tuner/epochs: 4
  - activation_1: leaky_relu
  - units_1: 20
  - activation_0: relu
  - tuner/round: 1
  - tuner/initial_epoch: 2
- Metrics:
  - accuracy: 0.5655384659767151
  - val_accuracy: 0.1936822086572647
  - val_AUC: 0.0
  - loss: 6.0173020362854
  - val_loss: 12.093679428100586
  - AUC: 0.5251981616020203
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - tensorflow_model

---

### Run: rogue-quail-739
- Run ID: 9fc5d4d5f7824f0397d76dfd49eb8008
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-28 21:57:15
- End Time: 2025-04-28 21:59:33
- Duration: 137.80 seconds
- Parameters:
  - optimizer: Adagrad
  - units_1: 44
  - lr: 0.001
  - activation_1: leaky_relu
  - num_layers: 1
  - units_0: 22
  - activation_0: leaky_relu
- Metrics:
  - loss: 1.1756081581115723
  - val_AUC: 0.0
  - accuracy: 0.5417807698249817
  - val_accuracy: 0.23066267371177673
  - AUC: 0.6078236103057861
  - val_loss: 2.149151086807251
- Artifacts:
  - AUC.jpg
  - accuracy.jpg
  - loss.jpg
  - tensorflow_model

---

### Run: beautiful-foal-873
- Run ID: 610f336bb89f45899af0d213ad71252f
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-04-28 20:53:35
- End Time: 2025-04-28 20:56:01
- Duration: 145.91 seconds
- Parameters:
  - units_1: 26
  - num_layers: 2
  - optimizer: Adam
  - lr: 0.001
  - activation_0: relu
  - activation_1: relu
  - units_0: 38
- Metrics:
  - None
- Artifacts:
  - tensorflow_model

---

### Run: unleashed-toad-225
- Run ID: bb85672082bc47f3b2667e0154f5c6bf
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-04-28 20:48:17
- End Time: 2025-04-28 20:50:36
- Duration: 138.01 seconds
- Parameters:
  - lr: 0.0001
  - activation_1: leaky_relu
  - num_layers: 2
  - units_0: 44
  - activation_0: relu
  - optimizer: Adam
  - units_1: 46
- Metrics:
  - None
- Artifacts:
  - tensorflow_model

---

### Run: bald-stag-799
- Run ID: 3b1600ad8c4f4e748e072c54de570289
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-04-28 20:41:54
- End Time: 2025-04-28 20:44:11
- Duration: 136.66 seconds
- Parameters:
  - activation_0: relu
  - num_layers: 1
  - lr: 0.0001
  - optimizer: Adam
  - units_0: 42
  - units_1: 26
  - activation_1: relu
- Metrics:
  - None
- Artifacts:
  - tensorflow_model

---

### Run: blushing-slug-480
- Run ID: ee893ad62a9c4e5dbb89e2976bd821bc
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-28 20:39:33
- End Time: 2025-04-28 20:39:47
- Duration: 14.56 seconds
- Parameters:
  - units_1: 30
  - units_0: 44
  - optimizer: Adagrad
  - num_layers: 1
  - lr: 0.0001
  - activation_1: leaky_relu
  - activation_0: relu
- Metrics:
  - None
- Artifacts:
  - tensorflow_model

---

### Run: marvelous-perch-117
- Run ID: 3bea46320a8948b093c1a2df1dedf27d
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-28 20:33:23
- End Time: 2025-04-28 20:33:38
- Duration: 14.91 seconds
- Parameters:
  - optimizer: Adam
  - activation_1: relu
  - units_0: 48
  - activation_0: relu
  - units_1: 32
  - lr: 0.0001
  - num_layers: 2
- Metrics:
  - None
- Artifacts:
  - tensorflow_model

---

### Run: trusting-cat-302
- Run ID: 51746ddb7c834326bdb80a834dcfd205
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-28 20:29:01
- End Time: 2025-04-28 20:29:02
- Duration: 1.39 seconds
- Parameters:
  - activation_0: leaky_relu
  - lr: 0.001
  - optimizer: Adam
  - num_layers: 1
  - units_0: 46
  - activation_1: relu
  - units_1: 32
- Metrics:
  - None
- Artifacts:
  - None

---

### Run: enthused-tern-250
- Run ID: 08d9bbaa5242484993e4475fc2284b2e
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-28 20:15:09
- End Time: 2025-04-28 20:16:04
- Duration: 55.28 seconds
- Parameters:
  - None
- Metrics:
  - None
- Artifacts:
  - None

---

## Experiment: foresight_xgb
- ID: 0
- Artifact Location: mlflow-artifacts:/d50540e3ebe24d678d06af45070629b7
- Lifecycle Stage: active

### Run: abundant-perch-550
- Run ID: 15d5749fbd0b4530b544f9729d13b84f
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:57:23
- End Time: 2025-05-18 18:04:59
- Duration: 455.70 seconds
- Parameters:
  - algorithm: kd_tree
  - leaf_size: 50
  - metric: minkowski
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.3813482125600179
  - std_fit_time: 0.013467000459032399
  - mean_score_time: 0.8193703492482504
  - std_score_time: 0.010459703691616064
  - mean_test_score: 0.6170862190634709
  - std_test_score: 0.00028843927810674454
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: intrigued-elk-817
- Run ID: 39218ee1c9ba45df95131a052a9a568e
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:57:23
- End Time: 2025-05-18 18:04:59
- Duration: 455.70 seconds
- Parameters:
  - algorithm: auto
  - leaf_size: 20
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 2
  - weights: distance
- Metrics:
  - mean_fit_time: 0.45244860649108887
  - std_fit_time: 0.03981876089540938
  - mean_score_time: 0.9355462392171224
  - std_score_time: 0.15127175294508385
  - mean_test_score: 0.6170862190634709
  - std_test_score: 0.00028843927810674454
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: luminous-panda-634
- Run ID: 514b68af9e6246c2899236f13e90dfc5
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:57:23
- End Time: 2025-05-18 18:04:59
- Duration: 455.70 seconds
- Parameters:
  - algorithm: ball_tree
  - leaf_size: 40
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.2889668146769206
  - std_fit_time: 0.0013597892362989955
  - mean_score_time: 0.691719134648641
  - std_score_time: 0.19539654309876112
  - mean_test_score: 0.6170862190634709
  - std_test_score: 0.00028843927810674454
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: upbeat-snake-646
- Run ID: 5996adfd40734825a8399f4731a4e12a
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:57:23
- End Time: 2025-05-18 18:05:21
- Duration: 477.87 seconds
- Parameters:
  - best_weights: distance
  - best_p: 1
  - best_n_neighbors: 5
  - best_metric: minkowski
  - best_leaf_size: 40
  - best_algorithm: kd_tree
  - cv: 3
  - error_score: nan
  - estimator: KNeighborsClassifier()
  - n_iter: 500
  - n_jobs: -1
  - param_distributions: {'n_neighbors': [3, 5, 7, 9, 11, 13], 'weights': ['uniform', 'distance'], 'algorithm': ['auto', 'kd_tree', 'ball_tree'], 'leaf_size': [20, 30, 40, 50], 'p': [1, 2], 'metric': ['euclidean', 'manhattan', 'minkowski']}
  - pre_dispatch: 2*n_jobs
  - random_state: 42
  - refit: True
  - return_train_score: False
  - scoring: f1_macro
  - verbose: 2
- Metrics:
  - training_precision_score: 1.0
  - training_recall_score: 1.0
  - training_f1_score: 1.0
  - training_accuracy_score: 1.0
  - training_log_loss: 2.2204460492503136e-16
  - training_roc_auc: 1.0
  - training_score: 1.0
  - best_cv_score: 0.6170862190634709
- Artifacts:
  - best_estimator
  - confusion_matrix.jpg
  - cv_results.csv
  - estimator.html
  - knn_model
  - model
  - training_confusion_matrix.png

---

### Run: industrious-bat-880
- Run ID: 5c1c41f722124fa5b25c169ffc66bd5a
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:57:23
- End Time: 2025-05-18 18:04:59
- Duration: 455.70 seconds
- Parameters:
  - algorithm: ball_tree
  - leaf_size: 50
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 2
  - weights: distance
- Metrics:
  - mean_fit_time: 0.282182772954305
  - std_fit_time: 0.011097784098372697
  - mean_score_time: 0.7988980611165365
  - std_score_time: 0.16393339023701053
  - mean_test_score: 0.6170862190634709
  - std_test_score: 0.00028843927810674454
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: persistent-finch-285
- Run ID: 8815784820fc40c19fd19f25facb7096
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:57:23
- End Time: 2025-05-18 18:04:59
- Duration: 455.70 seconds
- Parameters:
  - algorithm: kd_tree
  - leaf_size: 40
  - metric: minkowski
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.4712732632954915
  - std_fit_time: 0.05966354818384047
  - mean_score_time: 1.239372968673706
  - std_score_time: 0.1833125195554484
  - mean_test_score: 0.6170862190634709
  - std_test_score: 0.00028843927810674454
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: marvelous-owl-444
- Run ID: 108e479604c647b5b6792b7837a3ebb6
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:55:11
- End Time: 2025-05-18 18:03:07
- Duration: 475.69 seconds
- Parameters:
  - algorithm: kd_tree
  - leaf_size: 50
  - metric: minkowski
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.3767841657002767
  - std_fit_time: 0.013196278332559085
  - mean_score_time: 0.99734894434611
  - std_score_time: 0.28713095674797934
  - mean_test_score: 0.618102481518391
  - std_test_score: 0.0009448935043316654
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: indecisive-flea-298
- Run ID: 206ba7b8749a4e95be443e1f38c86d4d
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:55:11
- End Time: 2025-05-18 18:03:07
- Duration: 475.69 seconds
- Parameters:
  - algorithm: kd_tree
  - leaf_size: 40
  - metric: minkowski
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.3977855046590169
  - std_fit_time: 0.014514715561881358
  - mean_score_time: 0.9764106273651123
  - std_score_time: 0.15265959945362678
  - mean_test_score: 0.618102481518391
  - std_test_score: 0.0009448935043316654
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: placid-fawn-97
- Run ID: 6e42bf7406e9409b93f82714cc61ee83
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:55:11
- End Time: 2025-05-18 18:03:07
- Duration: 475.69 seconds
- Parameters:
  - algorithm: ball_tree
  - leaf_size: 40
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.2750050226847331
  - std_fit_time: 0.01736587686071333
  - mean_score_time: 0.6424569288889567
  - std_score_time: 0.13274414070618382
  - mean_test_score: 0.618102481518391
  - std_test_score: 0.0009448935043316654
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: resilient-stag-267
- Run ID: b680b2df72e744a09d114337cbb21555
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:55:11
- End Time: 2025-05-18 18:03:51
- Duration: 519.69 seconds
- Parameters:
  - cv: 3
  - error_score: nan
  - estimator: KNeighborsClassifier()
  - n_iter: 500
  - n_jobs: -1
  - param_distributions: {'n_neighbors': [3, 5, 7, 9, 11, 13], 'weights': ['uniform', 'distance'], 'algorithm': ['auto', 'kd_tree', 'ball_tree'], 'leaf_size': [20, 30, 40, 50], 'p': [1, 2], 'metric': ['euclidean', 'manhattan', 'minkowski']}
  - pre_dispatch: 2*n_jobs
  - random_state: 42
  - refit: True
  - return_train_score: False
  - scoring: f1_macro
  - verbose: 2
  - best_weights: distance
  - best_p: 1
  - best_n_neighbors: 5
  - best_metric: minkowski
  - best_leaf_size: 40
  - best_algorithm: kd_tree
- Metrics:
  - training_precision_score: 1.0
  - training_recall_score: 1.0
  - training_f1_score: 1.0
  - training_accuracy_score: 1.0
  - training_log_loss: 2.2204460492503136e-16
  - training_roc_auc: 1.0
  - training_score: 1.0
  - best_cv_score: 0.618102481518391
- Artifacts:
  - best_estimator
  - confusion_matrix.jpg
  - cv_results.csv
  - estimator.html
  - knn_model
  - model
  - training_confusion_matrix.png

---

### Run: serious-mouse-633
- Run ID: f5428ecea30145d19e7fb56562212327
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:55:11
- End Time: 2025-05-18 18:03:07
- Duration: 475.69 seconds
- Parameters:
  - algorithm: ball_tree
  - leaf_size: 50
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 2
  - weights: distance
- Metrics:
  - mean_fit_time: 0.2767640749613444
  - std_fit_time: 0.00770522018555583
  - mean_score_time: 0.575053850809733
  - std_score_time: 0.0369279325646473
  - mean_test_score: 0.618102481518391
  - std_test_score: 0.0009448935043316654
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: painted-dog-694
- Run ID: fdbc91c4476147ab9c79bed1ce8fdc1e
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:55:11
- End Time: 2025-05-18 18:03:07
- Duration: 475.69 seconds
- Parameters:
  - algorithm: auto
  - leaf_size: 20
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 2
  - weights: distance
- Metrics:
  - mean_fit_time: 0.425329049428304
  - std_fit_time: 0.04295836635086727
  - mean_score_time: 0.854201078414917
  - std_score_time: 0.13893243613610934
  - mean_test_score: 0.618102481518391
  - std_test_score: 0.0009448935043316654
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: redolent-eel-24
- Run ID: a258100876a443e488513d018f9ed657
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:43:58
- End Time: 2025-05-18 17:51:16
- Duration: 437.99 seconds
- Parameters:
  - algorithm: auto
  - leaf_size: 20
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 2
  - weights: distance
- Metrics:
  - mean_fit_time: 0.3972954750061035
  - std_fit_time: 0.018331629947983135
  - mean_score_time: 0.7388505935668945
  - std_score_time: 0.07865181519970983
  - mean_test_score: 0.6167195464921321
  - std_test_score: 0.0006605493349197354
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: tasteful-bug-884
- Run ID: a8aabbaf5a4f4224b7a20d101f2a0050
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:43:58
- End Time: 2025-05-18 17:51:38
- Duration: 459.98 seconds
- Parameters:
  - cv: 3
  - error_score: nan
  - estimator: KNeighborsClassifier()
  - n_iter: 500
  - n_jobs: -1
  - param_distributions: {'n_neighbors': [3, 5, 7, 9, 11, 13], 'weights': ['uniform', 'distance'], 'algorithm': ['auto', 'kd_tree', 'ball_tree'], 'leaf_size': [20, 30, 40, 50], 'p': [1, 2], 'metric': ['euclidean', 'manhattan', 'minkowski']}
  - pre_dispatch: 2*n_jobs
  - random_state: 42
  - refit: True
  - return_train_score: False
  - scoring: f1_macro
  - verbose: 2
  - best_weights: distance
  - best_p: 1
  - best_n_neighbors: 5
  - best_metric: minkowski
  - best_leaf_size: 40
  - best_algorithm: kd_tree
- Metrics:
  - training_precision_score: 1.0
  - training_recall_score: 1.0
  - training_f1_score: 1.0
  - training_accuracy_score: 1.0
  - training_log_loss: 2.2204460492503136e-16
  - training_roc_auc: 1.0
  - training_score: 1.0
  - best_cv_score: 0.6167195464921321
- Artifacts:
  - best_estimator
  - confusion_matrix.jpg
  - cv_results.csv
  - estimator.html
  - knn_model
  - model
  - training_confusion_matrix.png

---

### Run: serious-tern-530
- Run ID: b5fc93e207f64cadbba066fdd84e7087
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:43:58
- End Time: 2025-05-18 17:51:16
- Duration: 437.99 seconds
- Parameters:
  - algorithm: kd_tree
  - leaf_size: 40
  - metric: minkowski
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.3830614884694417
  - std_fit_time: 0.01881946285107826
  - mean_score_time: 0.9737587769826254
  - std_score_time: 0.03463827604817869
  - mean_test_score: 0.6167195464921321
  - std_test_score: 0.0006605493349197354
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: resilient-ram-158
- Run ID: c4bc4d71a5a94387aac5a388e5dc786e
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:43:58
- End Time: 2025-05-18 17:51:16
- Duration: 437.99 seconds
- Parameters:
  - algorithm: kd_tree
  - leaf_size: 50
  - metric: minkowski
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.3728521664937337
  - std_fit_time: 0.024364580990707332
  - mean_score_time: 0.7982891400655111
  - std_score_time: 0.06733069680973527
  - mean_test_score: 0.6167195464921321
  - std_test_score: 0.0006605493349197354
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: respected-ram-713
- Run ID: d9e60fe387e841e78dd8a52fc790adee
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:43:58
- End Time: 2025-05-18 17:51:16
- Duration: 437.99 seconds
- Parameters:
  - algorithm: ball_tree
  - leaf_size: 40
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 1
  - weights: distance
- Metrics:
  - mean_fit_time: 0.27667927742004395
  - std_fit_time: 0.008921200809625097
  - mean_score_time: 0.7710889975229899
  - std_score_time: 0.20357956636460578
  - mean_test_score: 0.6167195464921321
  - std_test_score: 0.0006605493349197354
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: bittersweet-moth-649
- Run ID: dfa091e662aa4a78b99d869871623dc5
- User: Jesolis14
- Status: FINISHED
- Start Time: 2025-05-18 17:43:58
- End Time: 2025-05-18 17:51:16
- Duration: 437.99 seconds
- Parameters:
  - algorithm: ball_tree
  - leaf_size: 50
  - metric: manhattan
  - metric_params: None
  - n_jobs: None
  - n_neighbors: 5
  - p: 2
  - weights: distance
- Metrics:
  - mean_fit_time: 0.26036572456359863
  - std_fit_time: 0.01489692050482162
  - mean_score_time: 0.7037911415100098
  - std_score_time: 0.12466384303050111
  - mean_test_score: 0.6167195464921321
  - std_test_score: 0.0006605493349197354
  - rank_test_score: 1.0
- Artifacts:
  - None

---

### Run: righteous-pug-914
- Run ID: 2b90610b993d40c6a34d77705486eddd
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-28 18:01:46
- End Time: 2025-04-28 18:04:44
- Duration: 177.67 seconds
- Parameters:
  - n_estimators: 200
  - max_depth: 15
  - colsample_bytree: 0.5
  - lr: 1e-05
- Metrics:
  - val_accuracy: 0.7782333333333333
  - train_accuracy: 0.8759159756532644
- Artifacts:
  - matriz.jpg
  - xgboost_model

---

### Run: fun-cub-43
- Run ID: db4dc35646a84975bc673149183c8fae
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-28 17:49:40
- End Time: 2025-04-28 17:52:16
- Duration: 155.63 seconds
- Parameters:
  - colsample_bytree: 0.5
  - n_estimators: 200
  - max_depth: 15
  - lr: 1e-05
- Metrics:
  - train_accuracy: 0.8733450814621014
  - val_accuracy: 0.7792666666666667
- Artifacts:
  - matriz.jpg

---

### Run: rebellious-crab-809
- Run ID: f391e79d01724b94a1ba08de16db0491
- User: MaAnCoSa
- Status: FINISHED
- Start Time: 2025-04-28 17:36:55
- End Time: 2025-04-28 17:39:38
- Duration: 163.21 seconds
- Parameters:
  - lr: 1e-05
  - max_depth: 15
  - colsample_bytree: 0.5
  - n_estimators: 200
- Metrics:
  - train_accuracy: 0.8745407959177054
  - val_accuracy: 0.77855
- Artifacts:
  - None

---

### Run: funny-flea-28
- Run ID: 3df5f48652674d78a12560136e7f7ed2
- User: MaAnCoSa
- Status: FAILED
- Start Time: 2025-04-28 17:29:55
- End Time: 2025-04-28 17:32:13
- Duration: 138.87 seconds
- Parameters:
  - colsample_bytree: 0.5
  - n_estimators: 200
  - max_depth: 15
  - lr: 1e-05
- Metrics:
  - None
- Artifacts:
  - None

---

