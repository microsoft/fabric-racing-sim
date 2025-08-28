# 🏎️ Fabric Racing Simulator - Real-time Racing Analytics Platform

**Ready to revolutionize your racing with real-time analytics?** 🏁

⭐ Star this repo if you find it useful!

🔄 Share it with fellow racers and data enthusiasts!

<p align="center">
  <b>Table of Contents</b><br>
  <a href="#-overview">Overview</a> •
  <a href="#-why-this-project-matters">Why This Project Matters</a> •
  <a href="#-key-features">Key Features</a> •
  <a href="#-technology-stack">Technology Stack</a> •
  <a href="#-prerequisites">Prerequisites</a> •
  <a href="#-setup-instructions">Setup Instructions</a> •
  <a href="#-sample-metrics-captured">Sample Metrics Captured</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

## 🚀 Overview

**Fabric Racing Simulator** is a showcase project that combines real-time telemetry from **Forza Motorsport** with the advanced analytics capabilities of **Microsoft Fabric**. This platform demonstrates how in-game racing data can be captured, processed, and visualized instantly using Microsoft Fabric Real-time Intelligence, turning your gameplay into actionable racing insights.

Imagine playing your favorite racing game while simultaneously capturing, processing, and visualizing every aspect of your performance in real-time. From telemetry data to lap times, from tire wear to Handbrakes – everything is streamed, stored, and displayed on stunning real-time dashboards.

### 🎯 Why This Project Matters

- **Real-world Data Engineering**: Learn how to build production-grade real-time data pipelines
- **Gaming Meets Analytics**: Bridge the gap between entertainment and professional data analytics
- **Microsoft Fabric Showcase**: Explore the full potential of Microsoft's unified analytics platform
- **Instant Insights**: Make data-driven decisions to improve your racing performance in real-time

## ✨ Key Features

### 📡 Real-time Data Ingestion

**UDP Network Listener**: High-performance client that captures telemetry data from Forza Motorsport, enrichies it and sends it to Microsoft Fabric

### 🔄 Intelligent Data Processing
- **Forza Data Parser**: Sophisticated parsing engine that understands Forza's telemetry format
- **Data enrichment**: Automatic calculation of derived metrics (lap deltas, sector times, optimal lines)
- **Stream processing**: Real-time data transformation and aggregation

### 📊 Microsoft Fabric Integration
- **Fabric Real-Time Intelligence**: Seamless integration with Microsoft Fabric's Real-time Intelligence
- **Auto-scaling**: Handles data spikes during intense racing moments
- **Long-term Storage**: Historical data retention for trend analysis and improvement tracking

### 📈 Live Performance Dashboard
- **Real-time visualizations**: See your data update as you race
- **Custom KPIs**: Track metrics that matter to you
- **Multi-session comparison**: Compare your performance across different races and tracks
- **Advanced visuals**: with Ploty integration

## 🛠️ Technology Stack

- **Data Ingestion**: UDP Network Protocol, .NET Desktop application
- **Stream Processing**: Microsoft Fabric Real-Time Intelligence
- **Data Storage**: Microsoft Fabric EventHouse + Lakehouse
- **Visualization**: Fabric Real-time Dashboards
- **Gaming Platform**: Forza Motorsport (Xbox/PC)

## 📋 Prerequisites

- ✅ **Microsoft Entra Tenant**
- ✅ **Forza Motorsport** on Xbox

## 🚦 Setup Instructions

### Part 1 - Set up Fabric

1. [Create a workspace in Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/fundamentals/create-workspaces). For this project, do not use the default "My Workspace". Name the workspace `Racing Sim`. 

2. [Assign a capacity to your workspace](https://learn.microsoft.com/en-us/fabric/fundamentals/workspace-license-mode). You can use a [trial capacity](https://learn.microsoft.com/en-us/fabric/fundamentals/fabric-trial).

3. Download the [Racing Sim Setup](https://github.com/microsoft/fabric-racing-sim/blob/main/setup/Racing%20Sim%20Setup.ipynb) notebook from this repo.

4. [Upload this notebook](https://learn.microsoft.com/en-us/fabric/data-engineering/how-to-use-notebook#import-existing-notebooks) into the workspace you created in a previous step. Run all the steps in the notebook.

5. In your workspace home page, Browse to the notebook entitled *RacingSim Generate Config*.

6. In the Notebook Exlporer, select **Resources**. You will see a file entitled *appsettings.json* under the **Built-in** folder. Download this file to your device.

### Part 2 - Set up the Forza Telemetry Client

1. From the [Forza Telemetry Client repo](https://github.com/toolboc/forza-telemetry-client/?tab=readme-ov-file#usage), under the **Usage** section, select the link to download and extract the latest release. 

2. Open the extracted folder, and open the subfolder named *config*. 

3. Replace the *appsettings.json* file with the contents of the *appsettings.json* file you downloaded from your Fabric workspace.

### Part 3 - Configure your game settings

1. Open the Forza Motorsport game and navigate to the settings menu.

2. Go to **Gameplay & HUD**
3. Under UDP Race Telemetery, [configure the following settings](https://www.youtube.com/watch?v=ThrJOwOPMhI):

    | Name                   | Setting                                                                                    |
    | ---------------------- | ------------------------------------------------------------------------------------------ |
    | Data Out               | On                                                                                         |
    | Data Out IP Address    | Enter the IP address of the computer on which you've installed the Forza Telemetry Client. |
    | Data Out IP Port       | 5300                                                                                       |
    | Data Out Packet Format | Car Dash                                                                                   |

4. Save and apply your changes.

5. Select the car for your game:

6. Set up the game using the following settings:

    | Name      | Setting     |
    | --------- | ----------- |
    | Game type | Circuit     |
    |     ??    | Short       |
    |     ??    | Silverstone |
    |     ??    | Grand prix  |

### Part 4 - Ready, set, play!

1. Run the Forza Telemetry Client application file from the extracted folder.

2. Start your game. You should immediately see telemetry data being captured and sent to your Fabric workspace both on the Telemetry Client and within the dashboards in your Fabric Real-Time Intelligence workspace. 

## 📊 Sample Metrics Captured

- 🏎️ **Vehicle Telemetry**: Speed, RPM, gear, throttle/brake input
- 🌡️ **Performance Data**: Engine temperature, tire wear, fuel consumption
- 📍 **Positional Data**: Track position, lap times, sector performance
- 🎮 **Driver Inputs**: Steering angle, throttle/brake pressure, gear changes
- 📈 **Calculated Metrics**: G-forces, slip angles, optimal racing line deviation

## 🤝 Contributing

We believe in the power of community! Whether you're fixing bugs, adding features, or improving documentation, your contributions are welcome.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
