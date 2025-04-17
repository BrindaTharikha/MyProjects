{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMIncmvOy8eCMN19jFa6Uvn",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/BrindaTharikha/MyProjects/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# app.py\n",
        "\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import joblib\n",
        "\n",
        "# Load trained model\n",
        "model = joblib.load(\"linear_regression_model.pkl\")\n",
        "\n",
        "st.title(\"Retail Price Prediction App\")\n",
        "\n",
        "# Input fields\n",
        "year = st.number_input(\"Year\", min_value=2000, max_value=2030, value=2024)\n",
        "month = st.selectbox(\"Month\", ['January', 'February', 'March', 'April', 'May', 'June',\n",
        "                               'July', 'August', 'September', 'October', 'November', 'December'])\n",
        "geo = st.selectbox(\"Geo\", ['Your GEO options here'])  # You can replace this with your actual unique GEOs\n",
        "product_category = st.selectbox(\"Product Category\", ['Your categories'])\n",
        "product = st.selectbox(\"Product\", ['Your products'])\n",
        "taxable = st.selectbox(\"Taxable\", ['Yes', 'No'])\n",
        "total_tax_rate = st.number_input(\"Total Tax Rate\", value=0.0)\n",
        "essential = st.selectbox(\"Essential\", [0, 1])\n",
        "coordinate = st.number_input(\"Coordinate\", value=0.0)\n",
        "uom = st.selectbox(\"Unit of Measure\", ['Your units'])\n",
        "\n",
        "# Prepare data for prediction\n",
        "input_df = pd.DataFrame([{\n",
        "    'Year': year,\n",
        "    'Month': month,\n",
        "    'GEO': geo,\n",
        "    'Product Category': product_category,\n",
        "    'Products': product,\n",
        "    'Taxable': taxable,\n",
        "    'Total tax rate': total_tax_rate,\n",
        "    'Essential': essential,\n",
        "    'COORDINATE': coordinate,\n",
        "    'UOM': uom\n",
        "}])\n",
        "\n",
        "# Predict\n",
        "if st.button(\"Predict\"):\n",
        "    prediction = model.predict(input_df)\n",
        "    st.success(f\"Predicted Value After Tax: ${prediction[0]:.2f}\")\n"
      ],
      "metadata": {
        "id": "G35XJRMZsoBZ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}