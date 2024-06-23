from mean_var_std import calculate

def test_calculate():
    # Define the test input list
    input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    # Call the calculate function
    result = calculate(input_list)
    
    # Print the result to verify correctness
    print("Result:", result)

    # Expected output for the given input list
    expected_output = {
        'mean': [
            [3.0, 4.0, 5.0],  # Mean along axis 0
            [1.0, 4.0, 7.0],  # Mean along axis 1
            4.0  # Mean of the flattened array
        ],
        'variance': [
            [6.0, 6.0, 6.0],  # Variance along axis 0
            [0.6666666666666666, 0.6666666666666666, 0.6666666666666666],  # Variance along axis 1
            6.666666666666667  # Variance of the flattened array
        ],
        'standard deviation': [
            [2.449489742783178, 2.449489742783178, 2.449489742783178],  # Std along axis 0
            [0.816496580927726, 0.816496580927726, 0.816496580927726],  # Std along axis 1
            2.581988897471611  # Std of the flattened array
        ],
        'max': [
            [6, 7, 8],  # Max along axis 0
            [2, 5, 8],  # Max along axis 1
            8  # Max of the flattened array
        ],
        'min': [
            [0, 1, 2],  # Min along axis 0
            [0, 3, 6],  # Min along axis 1
            0  # Min of the flattened array
        ],
        'sum': [
            [9, 12, 15],  # Sum along axis 0
            [3, 12, 21],  # Sum along axis 1
            36  # Sum of the flattened array
        ]
    }
    
    # Compare the result with the expected output
    assert result == expected_output, f"Test failed: {result} != {expected_output}"
    print("Test passed!")

if __name__ == "__main__":
    test_calculate()
