    model_formulas_1 <- c('yield_ana ~ tave5 + I(tave5^2) + tave6 + I(tave6^2) + tave7 + I(tave7^2) + FIPS', 'yield_ana ~ tave5 + I(tave5^2) + tave6 + I(tave6^2) + tave8 + I(tave8^2) + FIPS', 'yield_ana ~ tave5 + I(tave5^2) + tave6 + I(tave6^2) + tave9 + I(tave9^2) + FIPS', 'yield_ana ~ tave5 + I(tave5^2) + tave7 + I(tave7^2) + tave8 + I(tave8^2) + FIPS', 'yield_ana ~ tave5 + I(tave5^2) + tave7 + I(tave7^2) + tave9 + I(tave9^2) + FIPS', 'yield_ana ~ tave5 + I(tave5^2) + tave8 + I(tave8^2) + tave9 + I(tave9^2) + FIPS', 'yield_ana ~ tave6 + I(tave6^2) + tave7 + I(tave7^2) + tave8 + I(tave8^2) + FIPS', 'yield_ana ~ tave6 + I(tave6^2) + tave7 + I(tave7^2) + tave9 + I(tave9^2) + FIPS', 'yield_ana ~ tave6 + I(tave6^2) + tave8 + I(tave8^2) + tave9 + I(tave9^2) + FIPS', 'yield_ana ~ tave7 + I(tave7^2) + tave8 + I(tave8^2) + tave9 + I(tave9^2) + FIPS', 'yield_ana ~ tave5 + I(tave5^2) + tave6 + I(tave6^2) + tave7 + I(tave7^2) + tave8 + I(tave8^2) + FIPS', 'yield_ana ~ tave5 + I(tave5^2) + tave6 + I(tave6^2) + tave7 + I(tave7^2) + tave9 + I(tave9^2) + FIPS', 'yield_ana ~ tave5 + I(tave5^2) + tave6 + I(tave6^2) + tave8 + I(tave8^2) + tave9 + I(tave9^2) + FIPS', 'yield_ana ~ tave5 + I(tave5^2) + tave7 + I(tave7^2) + tave8 + I(tave8^2) + tave9 + I(tave9^2) + FIPS', 'yield_ana ~ tave6 + I(tave6^2) + tave7 + I(tave7^2) + tave8 + I(tave8^2) + tave9 + I(tave9^2) + FIPS', 'yield_ana ~ tave5 + I(tave5^2) + tave6 + I(tave6^2) + tave7 + I(tave7^2) + tave8 + I(tave8^2) + tave9 + I(tave9^2) + FIPS')


    model_names_1 <- c('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P')#4 
    
    fitting_functions_1 <- c("lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm")
    svd_issue_1 <- c("N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N")
    uses_FIPS_1 <- c("Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y")
    uses_evi_1 <- c("N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N")
    uses_lstmax_1 <- c("N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N")

    yield_prediction_csv_2 <- "./precip_potato.csv"
    rmse_csv_2 <- "./precip_potato_rmse.csv"

    model_formulas_2 <- c('yield_ana ~ precip5 + precip6 + precip7 + FIPS', 'yield_ana ~ precip5 + precip6 + precip8 + FIPS', 'yield_ana ~ precip5 + precip6 + precip9 + FIPS', 'yield_ana ~ precip5 + precip7 + precip8 + FIPS', 'yield_ana ~ precip5 + precip7 + precip9 + FIPS', 'yield_ana ~ precip5 + precip8 + precip9 + FIPS', 'yield_ana ~ precip6 + precip7 + precip8 + FIPS', 'yield_ana ~ precip6 + precip7 + precip9 + FIPS', 'yield_ana ~ precip6 + precip8 + precip9 + FIPS', 'yield_ana ~ precip7 + precip8 + precip9 + FIPS', 'yield_ana ~ precip5 + precip6 + precip7 + precip8 + FIPS', 'yield_ana ~ precip5 + precip6 + precip7 + precip9 + FIPS', 'yield_ana ~ precip5 + precip6 + precip8 + precip9 + FIPS', 'yield_ana ~ precip5 + precip7 + precip8 + precip9 + FIPS', 'yield_ana ~ precip6 + precip7 + precip8 + precip9 + FIPS', 'yield_ana ~ precip5 + precip6 + precip7 + precip8 + precip9 + FIPS')


    model_names_2 <- c('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P')#4 
    
    fitting_functions_2 <- c("lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm")
    svd_issue_2 <- c("N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N")
    uses_FIPS_2 <- c("Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y")
    uses_evi_2 <- c("N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N")
    uses_lstmax_2 <- c("N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N")


    yield_prediction_csv_3 <- "./vpdave_potato.csv"
    rmse_csv_3 <- "./vpdave_potato_rmse.csv"

    model_formulas_3 <- c('yield_ana ~ vpdave5 + vpdave6 + vpdave7 + FIPS', 'yield_ana ~ vpdave5 + vpdave6 + vpdave8 + FIPS', 'yield_ana ~ vpdave5 + vpdave6 + vpdave9 + FIPS', 'yield_ana ~ vpdave5 + vpdave7 + vpdave8 + FIPS', 'yield_ana ~ vpdave5 + vpdave7 + vpdave9 + FIPS', 'yield_ana ~ vpdave5 + vpdave8 + vpdave9 + FIPS', 'yield_ana ~ vpdave6 + vpdave7 + vpdave8 + FIPS', 'yield_ana ~ vpdave6 + vpdave7 + vpdave9 + FIPS', 'yield_ana ~ vpdave6 + vpdave8 + vpdave9 + FIPS', 'yield_ana ~ vpdave7 + vpdave8 + vpdave9 + FIPS', 'yield_ana ~ vpdave5 + vpdave6 + vpdave7 + vpdave8 + FIPS', 'yield_ana ~ vpdave5 + vpdave6 + vpdave7 + vpdave9 + FIPS', 'yield_ana ~ vpdave5 + vpdave6 + vpdave8 + vpdave9 + FIPS', 'yield_ana ~ vpdave5 + vpdave7 + vpdave8 + vpdave9 + FIPS', 'yield_ana ~ vpdave6 + vpdave7 + vpdave8 + vpdave9 + FIPS', 'yield_ana ~ vpdave5 + vpdave6 + vpdave7 + vpdave8 + vpdave9 + FIPS')


    model_names_3 <- c('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P')#4 
    
    fitting_functions_3 <- c("lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm")
    svd_issue_3 <- c("N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N")
    uses_FIPS_3 <- c("Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y")
    uses_evi_3 <- c("N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N")
    uses_lstmax_3 <- c("N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N")


    #___________________________________
    # Give names to the CSVs in which we will, firstly, store the results of predictions and, secondly, in which we will store the RMSEs that we calculate for these
    # predictions.

    yield_prediction_csv_1 <- "./yan_combinations_potato.csv"
    rmse_csv_1 <- "./yan_combinations_potato_rmse.csv"

    # Specify the model formulas that we wish to test
    model_formulas_1 <- c("yield_ana ~ vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + precip5 +  precip6 +  precip7 +  precip8 + FIPS", "yield_ana ~ vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + precip5 +  precip6 +  precip7 +  precip8 + I(precip5^2) + I(precip6^2) + I(precip7^2) + I(precip8^2) + FIPS", "yield_ana ~ vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + I(vpdave5^2) + I(vpdave6^2) + I(vpdave7^2) + I(vpdave8^2) + precip5 +  precip6 +  precip7 +  precip8 + FIPS", "yield_ana ~ vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + I(vpdave5^2) + I(vpdave6^2) + I(vpdave7^2) + I(vpdave8^2) + precip5 +  precip6 +  precip7 +  precip8 + I(precip5^2) + I(precip6^2) + I(precip7^2) + I(precip8^2) + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + precip5 +  precip6 +  precip7 +  precip8 + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + precip5 +  precip6 +  precip7 +  precip8 + I(precip5^2) + I(precip6^2) + I(precip7^2) + I(precip8^2) + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + I(tave5^2) + I(tave6^2) + I(tave7^2) + I(tave8^2) + precip5 +  precip6 +  precip7 +  precip8 + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + I(tave5^2) + I(tave6^2) + I(tave7^2) + I(tave8^2) + precip5 +  precip6 +  precip7 +  precip8 + I(precip5^2) + I(precip6^2) + I(precip7^2) + I(precip8^2) + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + precip5 +  precip6 +  precip7 +  precip8 + vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + precip5 +  precip6 +  precip7 +  precip8 + I(precip5^2) + I(precip6^2) + I(precip7^2) + I(precip8^2) + vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + I(tave5^2) + I(tave6^2) + I(tave7^2) + I(tave8^2) + precip5 +  precip6 +  precip7 +  precip8 + vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + I(tave5^2) + I(tave6^2) + I(tave7^2) + I(tave8^2) + precip5 +  precip6 +  precip7 +  precip8 + I(precip5^2) + I(precip6^2) + I(precip7^2) + I(precip8^2) + vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + precip5 +  precip6 +  precip7 +  precip8 + vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + I(vpdave5^2) + I(vpdave6^2) + I(vpdave7^2) + I(vpdave8^2) + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + precip5 +  precip6 +  precip7 +  precip8 + I(precip5^2) + I(precip6^2) + I(precip7^2) + I(precip8^2) + vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + I(vpdave5^2) + I(vpdave6^2) + I(vpdave7^2) + I(vpdave8^2) + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + I(tave5^2) + I(tave6^2) + I(tave7^2) + I(tave8^2) + precip5 +  precip6 +  precip7 +  precip8 + vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + I(vpdave5^2) + I(vpdave6^2) + I(vpdave7^2) + I(vpdave8^2) + FIPS", "yield_ana ~ tave5 +  tave6 +  tave7 +  tave8 + I(tave5^2) + I(tave6^2) + I(tave7^2) + I(tave8^2) + precip5 +  precip6 +  precip7 +  precip8 + I(precip5^2) + I(precip6^2) + I(precip7^2) + I(precip8^2) + vpdave5 +  vpdave6 +  vpdave7 +  vpdave8 + I(vpdave5^2) + I(vpdave6^2) + I(vpdave7^2) + I(vpdave8^2)")


    # For each of the model formulas that we specified above, give each model configuration a name
    model_names_1 <- c('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P')
    
    # For each of the model formulas, determine whether we will fit the model using lm or using lmer
    # Note that lm is the ordinary OLS function and lmer the hierarchical model function
    fitting_functions_1 <- c("lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm","lm")

    # For each of the model formulas, specify whether the model formula uses FIPS or not, and then evi and then lst
    uses_FIPS_1 <- c("Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y")
    uses_evi_1 <- c("N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N")
    uses_lstmax_1 <- c("N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N")


    # Each of the following list suffixed variables is a list that stores as many variables as model experiments that we want to run
    # By model experiment, I refer to the collection of model configurations that one wants to test in one run of this code.
    # For example, we may wish to test model configurations using precip in one run and then model configurations using tave in another run
    # The model configurations, within the model experiment, using precip may be yield ~ precip5 + precip6 + precip7 + FIPS or yield ~ precip6 + precip7 + precip8 + FIPS

    yield_prediction_csv_list <- list(yield_prediction_csv_1)
    rmse_csv_list <- list(rmse_csv_1)
    model_formulas_list <- list(model_formulas_1)
    model_names_list <- list(model_names_1)
    fitting_functions_list <- list(fitting_functions_1)
    uses_evi_list <- list(uses_evi_1)
    uses_lstmax_list <- list(uses_lstmax_1)
    uses_FIPS_list <- list(uses_FIPS_1)

