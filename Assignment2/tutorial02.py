# All decimal 3 places
import math

# Function to compute mean
def mean(first_list):
    # mean Logic 
    list_size = len(first_list)
    if(list_size==0):
        return 0
    for item in first_list:
        if(not isinstance(item,(int,float))):
            return 0
    total_sum = summation(first_list)
    mean_value = total_sum/list_size
    mean_value = round(mean_value,3)
    return mean_value


# Function to compute median. You cant use Python functions
# def median(first_list):
#     # median Logic
#     return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    list_size = len(first_list)
    if(list_size==0):
        return 0
    for item in first_list:
        if(not isinstance(item,(int,float))):
            return 0
    
    mean_first_list = mean(first_list)
    modified_list = [] #list with item values as square of (item value of first list - mean of first list)

    for item in first_list:
        modified_list.append((item - mean_first_list)*(item - mean_first_list))
    
    modified_list_sum = summation(modified_list)
    standard_deviation_value = math.sqrt(modified_list_sum/list_size)
    standard_deviation_value = round(standard_deviation_value,3)
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    list_size = len(first_list)
    if(list_size==0):
        return 0
    for item in first_list:
        if(not isinstance(item,(int,float))):
            return 0
    
    mean_first_list = mean(first_list)
    modified_list = [] #list with item values as square of (item value of first list - mean of first list)

    for item in first_list:
        modified_list.append((item - mean_first_list)*(item - mean_first_list))
    
    modified_list_sum = summation(modified_list)
    variance_value = modified_list_sum/list_size
    variance_value = round(variance_value,3)
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    first_list_size = len(first_list)
    second_list_size = len(second_list)

    if(first_list_size != second_list_size):
        return 0
    
    for item1,item2 in zip(first_list,second_list):
        if((not isinstance(item1,(int,float))) or (not isinstance(item2,(int,float)))):
            return 0
    
    modified_list = [] #list with item values as square of (item value of first list - item value of second list)

    for item1,item2 in zip(first_list,second_list):
        modified_list.append((item1 - item2)*(item1 - item2))
    
    modified_list_sum = summation(modified_list)
    rmse_value = modified_list_sum/first_list_size
    rmse_value = math.sqrt(rmse_value)
    rmse_value = round(rmse_value,3)    
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    first_list_size = len(first_list)
    second_list_size = len(second_list)

    if(first_list_size!=second_list_size):
        return 0
    
    for item1,item2 in zip(first_list,second_list):
        if((not isinstance(item1,(int,float))) or (not isinstance(item2,(int,float)))):
            return 0
    
    modified_list = [] #list with item values as square of (item value of first list - item value of second list)

    for item1,item2 in zip(first_list,second_list):
        modified_list.append((item1 - item2)*(item1 - item2))
    
    modified_list_sum = summation(modified_list)
    mse_value = modified_list_sum/first_list_size
    mse_value = round(mse_value,3)    
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    first_list_size = len(first_list)
    second_list_size = len(second_list)

    if(first_list_size != second_list_size):
        return 0
    
    for item1,item2 in zip(first_list,second_list):
        if((not isinstance(item1,(int,float))) or (not isinstance(item2,(int,float)))):
            return 0
    
    modified_list = [] #list with item values as abs of (item value of first list - item value of second list)

    for item1,item2 in zip(first_list,second_list):
        modified_list.append(abs(item1 - item2))
    
    modified_list_sum = summation(modified_list)
    mae_value = modified_list_sum/first_list_size
    mae_value = round(mae_value,3)    
    return mae_value


# # Function to compute NSE. You cant use Python functions
# def nse(first_list, second_list):
#     # nse Logic
#     return nse_value


# # Function to compute Pearson correlation coefficient. You cant use Python functions
# def pcc(first_list, second_list):
#     # nse Logic
#     return pcc_value


# # Function to compute Skewness. You cant use Python functions
# def skewness(first_list):
#     # Skewness Logic
#     return skewness_value
    
# def sorting(first_list):
#     # Sorting Logic
#     return sorted_list


# # Function to compute Kurtosis. You cant use Python functions
# def kurtosis(first_list):
#     # Kurtosis Logic
#     return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value=0
    for item in first_list:
        summation_value+=item
    return summation_value
