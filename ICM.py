{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sai-2421/project_4/blob/main/ICM.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "collapsed": true,
        "id": "OvVXvhBd7MVl"
      },
      "outputs": [],
      "source": [
        "!pip install streamlit pyngrok\n",
        "!pip install streamlit streamlit-option-menu pyngrok\n",
        "\n",
        "!pip install scikit-learn==1.3.2\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "H-6525gfIx3j"
      },
      "outputs": [],
      "source": [
        "# Run the Streamlit app and expose it via ngrok\n",
        "from pyngrok import ngrok"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dgOHT81PI4rU",
        "outputId": "0dff17b2-6636-44af-e419-4bd5a5c8ed24"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml\n"
          ]
        }
      ],
      "source": [
        "!ngrok authtoken 2lNSHX18CGUMfvIF6K8BaLLGbUH_3L16UBv5AHV5kBvtHAF8H"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-qXFdugQ7o9A",
        "outputId": "6e1898fc-5e96-4e73-f714-63dab5d521f6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing icm.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile icm.py\n",
        "\n",
        "import streamlit as st\n",
        "from streamlit_option_menu import option_menu\n",
        "import numpy as np\n",
        "import pickle\n",
        "# -------------------------------Configuration for Streamlit Application---------------------------\n",
        "st.set_page_config(\n",
        "    page_title=\"Industrial Copper Modeling\",\n",
        "    page_icon=\"🏨\",\n",
        "    layout=\"wide\"\n",
        ")\n",
        "\n",
        "# -------------------------------Sidebar for Navigation--------------------\n",
        "with st.sidebar:\n",
        "    selected = option_menu(\"Main Menu\", [\"About Project\", \"Selling Price Prediction\", \"Status Prediction\"],\n",
        "                           icons=[\"house\", \"gear\", \"gear\"],\n",
        "                           styles={\n",
        "                               \"nav-link\": {\"font\": \"sans serif\", \"font-size\": \"20px\", \"text-align\": \"centre\"},\n",
        "                               \"nav-link-selected\": {\"font\": \"sans serif\", \"background-color\": \"#98FB98\"},\n",
        "                               \"icon\": {\"font-size\": \"20px\"}\n",
        "                           }\n",
        "                           )\n",
        "\n",
        "# -----------------------------------About Project Section--------------------------------------------------\n",
        "if selected == \"About Project\":\n",
        "    st.markdown(\"# :green[Industrial Copper Modeling]\")\n",
        "    st.markdown('<div style=\"height: 50px;\"></div>', unsafe_allow_html=True)\n",
        "    st.markdown(\"### :green[Technologies :] Python, Pandas, Numpy, Scikit-Learn, Streamlit, Machine Learning, Data Preprocessing, Visualization, EDA, Model Building, Model Deployment\")\n",
        "    st.markdown(\"### :green[Overview :] Like many other industries, the copper sector struggles with distorted and noisy sales and pricing data. Manual forecasting is time-consuming and may lack precision. By leveraging machine learning techniques, we can significantly enhance decision-making, addressing issues like skewness and noise in the data. We will create a regression model to forecast selling prices and a classification algorithm to predict lead status (WON or LOST) based on historical transactions.\")\n",
        "\n",
        "# ------------------------------------------------Predictions Section---------------------------------------------------\n",
        "if selected == \"Selling Price Prediction\":\n",
        "    st.markdown(\"# :green[Predicting Results based on Trained Model]\")\n",
        "\n",
        "    # -----New Data inputs from the user for predicting the selling price-----\n",
        "    inputs = {\n",
        "        \"Quantity\": st.text_input(\"Quantity\"),\n",
        "        \"Status\": st.text_input(\"Status\"),\n",
        "        \"Item Type\": st.text_input(\"Item Type\"),\n",
        "        \"Application\": st.text_input(\"Application\"),\n",
        "        \"Thickness\": st.text_input(\"Thickness\"),\n",
        "        \"Width\": st.text_input(\"Width\"),\n",
        "        \"Country\": st.text_input(\"Country\"),\n",
        "        \"Customer\": st.text_input(\"Customer\"),\n",
        "        \"Product Reference\": st.text_input(\"Product Reference\")\n",
        "    }\n",
        "\n",
        "\n",
        "\n",
        "    # Correctly define the file path without including 'rb' in the path variable\n",
        "    pickle_file_path_1 = r\"/content/regression_model.pkl\"\n",
        "\n",
        "    # Now open and load the model using 'rb' mode\n",
        "    with open(pickle_file_path_1, 'rb') as file_1:\n",
        "      regression_model =pickle.load(file_1)\n",
        "\n",
        "\n",
        "    # -----Submit Button for Predicting Selling Price-----\n",
        "    predict_button_1 = st.button(\"Predict Selling Price\")\n",
        "\n",
        "    if predict_button_1:\n",
        "        try:\n",
        "            # Convert inputs to appropriate types\n",
        "            new_sample_1 = np.array([[np.log(float(inputs[\"Quantity\"])),\n",
        "                                       float(inputs[\"Status\"]),\n",
        "                                       float(inputs[\"Item Type\"]),\n",
        "                                       float(inputs[\"Application\"]),\n",
        "                                       np.log(float(inputs[\"Thickness\"])),\n",
        "                                       float(inputs[\"Width\"]),\n",
        "                                       float(inputs[\"Country\"]),\n",
        "                                       float(inputs[\"Customer\"]),\n",
        "                                       float(inputs[\"Product Reference\"])]])\n",
        "            new_pred_1 = regression_model.predict(new_sample_1)[0]\n",
        "            st.write('Result: Predicted selling price: ', np.exp(new_pred_1))\n",
        "\n",
        "        except ValueError:\n",
        "            st.error(\"Please enter valid numeric inputs.\")\n",
        "\n",
        "if selected == \"Status Prediction\":\n",
        "    st.markdown(\"# :green[Predicting Results based on Trained Model]\")\n",
        "\n",
        "    # -----New Data inputs from the user for predicting the status-----\n",
        "    inputs_status = {\n",
        "        \"Quantity\": st.text_input(\"Quantity\"),\n",
        "        \"Selling Price\": st.text_input(\"Selling Price\"),\n",
        "        \"Item Type\": st.text_input(\"Item Type\"),\n",
        "        \"Application\": st.text_input(\"Application\"),\n",
        "        \"Thickness\": st.text_input(\"Thickness\"),\n",
        "        \"Width\": st.text_input(\"Width\"),\n",
        "        \"Country\": st.text_input(\"Country\"),\n",
        "        \"Customer\": st.text_input(\"Customer\"),\n",
        "        \"Product Reference\": st.text_input(\"Product Reference\")\n",
        "    }\n",
        "\n",
        "    pickle_file_path_1=r\"/content/classfier_model.pkl\"\n",
        "\n",
        "\n",
        "    with open(pickle_file_path_1, 'rb') as file_2:\n",
        "        classification_model = pickle.load(file_2)\n",
        "\n",
        "    # -----Submit Button for Predicting Status-----\n",
        "    predict_button_2 = st.button(\"Predict Status\")\n",
        "\n",
        "    if predict_button_2:\n",
        "        try:\n",
        "            new_sample_2 = np.array([[np.log(float(inputs_status[\"Quantity\"])),\n",
        "                                       np.log(float(inputs_status[\"Selling Price\"])),\n",
        "                                       float(inputs_status[\"Item Type\"]),\n",
        "                                       float(inputs_status[\"Application\"]),\n",
        "                                       np.log(float(inputs_status[\"Thickness\"])),\n",
        "                                       float(inputs_status[\"Width\"]),\n",
        "                                       float(inputs_status[\"Country\"]),\n",
        "                                       float(inputs_status[\"Customer\"]),\n",
        "                                       float(inputs_status[\"Product Reference\"])]])\n",
        "            new_pred_2 = classification_model.predict(new_sample_2)\n",
        "\n",
        "            if new_pred_2 == 1:\n",
        "                st.write('Result: The Status is: Won')\n",
        "            else:\n",
        "                st.write('Result: The Status is: Lost')\n",
        "\n",
        "        except ValueError:\n",
        "            st.error(\"Please enter valid numeric inputs.\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A4p5JSBJGulA",
        "outputId": "88cbcf99-e9a5-426e-95d1-fb2cc1a51280"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Streamlit app is live at: NgrokTunnel: \"https://32ba-35-185-135-22.ngrok-free.app\" -> \"http://localhost:8501\"\n"
          ]
        }
      ],
      "source": [
        "# Expose the Streamlit app to the web using ngrok\n",
        "public_url = ngrok.connect(8501, \"http\")\n",
        "print(f\"Streamlit app is live at: {public_url}\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "Sze0PkpkCrD3",
        "outputId": "305591cc-f6b8-4465-dff3-4e9f1f18af7a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://35.185.135.22:8501\u001b[0m\n",
            "\u001b[0m\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:465: UserWarning: X does not have valid feature names, but RandomForestRegressor was fitted with feature names\n",
            "  warnings.warn(\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:465: UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names\n",
            "  warnings.warn(\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:pyngrok.process.ngrok:t=2024-09-26T07:04:12+0000 lvl=warn msg=\"Stopping forwarder\" name=http-8501-79192472-b444-4799-87ca-d924fb8b5d8f acceptErr=\"failed to accept connection: Listener closed\"\n",
            "WARNING:pyngrok.process.ngrok:t=2024-09-26T07:04:12+0000 lvl=warn msg=\"Error restarting forwarder\" name=http-8501-79192472-b444-4799-87ca-d924fb8b5d8f err=\"failed to start tunnel: session closed\"\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[34m  Stopping...\u001b[0m\n",
            "\u001b[34m  Stopping...\u001b[0m\n"
          ]
        }
      ],
      "source": [
        "# Start the Streamlit app\n",
        "!streamlit run icm.py"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMgFFwxDoV3WJJoCiti35rw",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}