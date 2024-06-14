import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Define the combined true and predicted labels
true_labels = ['personal'] * 100 + ['social'] * 100 + ['professional'] * 100
predicted_labels = (
    ['personal'] * 79 + ['social'] * 19 + ['professional'] * 2 +  # Predictions for true 'personal'
    ['personal'] * 4 + ['social'] * 83 + ['professional'] * 13 +  # Predictions for true 'social'
    ['personal'] * 1 + ['social'] * 14 + ['professional'] * 85  # Predictions for true 'professional'
)

# Convert labels to a format suitable for confusion matrix computation
unique_labels = ['personal', 'social', 'professional']
true_labels_numeric = [unique_labels.index(label) for label in true_labels]
predicted_labels_numeric = [unique_labels.index(label) for label in predicted_labels]

# Compute the confusion matrix
cm = confusion_matrix(true_labels_numeric, predicted_labels_numeric, labels=[0, 1, 2])

# Display the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=unique_labels)
disp.plot(cmap=plt.cm.Blues)

# Show the plot
plt.show()
