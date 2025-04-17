{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPrtJIIA1ub+CN5XhBzZZ1k",
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
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 393
        },
        "id": "2aRY7a_1t85I",
        "outputId": "06c010f4-461e-46ee-da39-fc05c3a51e82"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'streamlit'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-4e4f9762f3fa>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# app.py\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mjoblib\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "cbErsRLwC6Fr"
      },
      "outputs": [],
      "source": [
        "app_code = \"\"\"\n",
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
        "geo = st.selectbox(\"Geo\", ['Ontario', 'Alberta', 'Quebec'])  # Replace with your real GEOs\n",
        "product_category = st.selectbox(\"Product Category\", ['Vegetables', 'Fruits'])  # Example categories\n",
        "product = st.selectbox(\"Product\", ['Potatoes, per kilogram', 'Bananas, per kilogram'])\n",
        "taxable = st.selectbox(\"Taxable\", ['Yes', 'No'])\n",
        "total_tax_rate = st.number_input(\"Total Tax Rate\", value=0.0)\n",
        "essential = st.selectbox(\"Essential\", [0, 1])\n",
        "coordinate = st.number_input(\"Coordinate\", value=0.0)\n",
        "uom = st.selectbox(\"Unit of Measure\", ['per kilogram', 'per litre'])\n",
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
        "    st.success(f\"Predicted Value After Tax: ${prediction[0]:.2f}\")\n",
        "\"\"\"\n"
      ]
    }
  ]
}