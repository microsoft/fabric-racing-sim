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
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-sample-metrics-captured">Sample Metrics Captured</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>

## 🚀 Overview

**Fabric Racing Simulator** is a showcase project that combines real-time telemetry from **Forza Motorsport** with the advanced analytics capabilities of **Microsoft Fabric**. This platform demonstrates how in-game racing data can be captured, processed, and visualized instantly using Microsoft Fabric Real-time Intelligence (RTI), turning your gameplay into actionable racing insights.

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
- **Data Enrichment**: Automatic calculation of derived metrics (lap deltas, sector times, optimal lines)
- **Stream Processing**: Real-time data transformation and aggregation

### 📊 Microsoft Fabric Integration
- **Fabric RTI**: Seamless integration with Microsoft Fabric's Real-time Intelligence
- **Auto-scaling**: Handles data spikes during intense racing moments
- **Long-term Storage**: Historical data retention for trend analysis and improvement tracking

### 📈 Live Performance Dashboard
- **Real-time Visualizations**: See your data update as you race
- **Custom KPIs**: Track metrics that matter to you
- **Multi-session Comparison**: Compare your performance across different races and tracks
- **Advanced visuals**: with Ploty integration

## 🛠️ Technology Stack

- **Data Ingestion**: UDP Network Protocol, .NET Desktop application
- **Stream Processing**: Microsoft Fabric Real-time Intelligence
- **Data Storage**: Microsoft Fabric EventHouse + Lakehouse
- **Visualization**: Fqbric Real-time Dashboards
- **Gaming Platform**: Forza Motorsport (Xbox/PC)

## 📋 Prerequisites

- ✅ **Microsoft Entra Tenant** with Fabric workspace and capacity (trial works!)
- ✅ **Forza Motorsport** on Xbox or PC or **Forza Data Simulator** (included in this repository)
- ✅ **Network Configuration** to enable UDP telemetry output
- ✅ **Basic knowledge** of data streaming concepts (we'll guide you through the rest!)

## 🚦 Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/microsoft/fabric-racing-sim.git
   cd fabric-racing-sim
   ```

2. **Configure Forza Motorsport**
   - Enable UDP telemetry output in game settings
   - Set the appropriate IP and port configuration

or 
    - Use the included **Forza Data Simulator** to generate test data
    
    > **Note**: Forza Data Simulator is a .NET application that simulates telemetry data for testing purposes.

3. **Set Up Microsoft Fabric**
   - See [Fabric Setup guide](docs/setup-fabric.md) for detailed instructions

4. **Launch the Client**
   ```bash
   # Start the UDP listener and Fabric connector
   ./start-racing-analytics.sh
   ```

5. **Start Racing!**
   - Launch Forza Motorsport and start a race
   - Watch your data flow in real-time on the dashboard

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
