# Mr. Wright Adventures - Strategy & Business Development Platform

A comprehensive business strategy website for Mr. Wright Adventures, a premium travel concierge and logistics platform serving Costa Rica's tourism market.

![Mr. Wright Adventures](https://img.shields.io/badge/Status-Production%20Ready-green)
![License](https://img.shields.io/badge/License-Proprietary-red)

## 🌟 Overview

This full-stack web application presents a complete business strategy package including:

- **Business Model Canvas** - Strategic framework and value propositions
- **Market Analysis** - Costa Rica tourism infrastructure and competitive landscape
- **Operational Playbooks** - Detailed SOPs and workflow diagrams
- **Unit Economics** - Financial modeling and pricing analysis
- **Investment Scenarios** - Interactive capital deployment models with game theory
- **Experience Journeys** - Persona-driven customer journey narratives
- **Marketing Strategy** - Audience-specific messaging and content guides

## 🚀 Features

### Interactive Sections

#### 💡 Investment Scenarios
- 4 investment levels ($10K, $20K, $30K, $50K)
- Game theory positioning (Conservative → Aggressive)
- Dynamic ROI calculations (62% - 201%)
- Capital deployment visualizations
- Risk-reward analysis

#### 🎒 Experience Journeys
- 3 detailed personas (Family, Couple, Solo Traveler)
- Emotional journey visualizations
- Cost & profit breakdowns by touchpoint
- Behind-the-scenes operations view

### Downloadable Resources
- 17 comprehensive strategy documents
- 11 data visualizations and charts
- Operational workflow diagrams
- Market research and analysis

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI framework
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Lucide React** - Icons

### Backend
- **Flask** - Python web framework
- **SQLAlchemy** - Database ORM
- **Python 3.11** - Runtime

### Data Visualization
- **Matplotlib** - Chart generation
- **NumPy** - Data processing

## 📁 Project Structure

```
mr-wright-v3/
├── src/
│   ├── main.py                 # Flask application entry point
│   ├── routes/
│   │   ├── downloads.py        # Document download endpoints
│   │   └── user.py             # User management routes
│   ├── models/
│   │   └── user.py             # Database models
│   └── static/                 # Frontend build output
│       ├── index.html          # React app entry
│       ├── assets/             # JS/CSS bundles
│       └── documents/          # Strategy documents & visualizations
├── requirements.txt            # Python dependencies
└── venv/                       # Virtual environment
```

## 🚦 Getting Started

### Prerequisites
- Python 3.11+
- Node.js 22+ (for frontend development)
- pnpm (for frontend package management)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/LenoxSaintGermain/mr-wright-adventures.git
cd mr-wright-adventures
```

2. **Set up Python virtual environment**
```bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Run the application**
```bash
python src/main.py
```

4. **Access the application**
Open your browser to `http://localhost:5000`

## 📊 Business Metrics

### Market Opportunity
- **2.66M** annual visitors to Costa Rica (2024)
- **54%** from United States
- **36%** average gross margin across services
- **$59.8K** monthly revenue potential at scale

### Service Offerings
1. **VIP Airport Transfers** - 42.5% margin
2. **Concierge Services** - 33.3% margin
3. **Helicopter Charters** - 27.3% margin

### Investment Scenarios
| Capital | ROI (12mo) | Breakeven | Monthly Revenue |
|---------|-----------|-----------|-----------------|
| $10K    | 62%       | 7.4 mo    | $3,750          |
| $20K    | 104%      | 6.9 mo    | $8,000          |
| $30K    | 147%      | 6.1 mo    | $13,200         |
| $50K    | 201%      | 5.9 mo    | $22,100         |

## 📖 Documentation

### Strategy Documents
- [Business Model Canvas](src/static/documents/business_model_canvas.md)
- [Operational Manual](src/static/documents/operational_manual_master.md)
- [Product Requirements](src/static/documents/prd.md)
- [Market Context](src/static/documents/costa_rica_market_context.md)
- [Unit Economics](src/static/documents/unit_economics_analysis.md)

### Operational Resources
- [Partnership Framework](src/static/documents/partnership_framework.md)
- [Resource Management](src/static/documents/resource_management_plan.md)
- [Journey Maps](src/static/documents/journey_maps.md)
- [Workflow Diagrams](src/static/documents/workflow_diagrams.md)
- [Pre-Launch Checklist](src/static/documents/readiness_checklist.md)

## 🎨 Design System

### Color Palette
- **Primary Blue**: #3B82F6
- **Success Green**: #10B981
- **Warning Orange**: #F59E0B
- **Purple Accent**: #8B5CF6
- **Indigo**: #6366F1

### Typography
- **Font Family**: System UI stack (Inter, SF Pro, Segoe UI)
- **Headings**: Bold, large scale
- **Body**: Regular weight, comfortable line height

## 🔒 Security & Privacy

- No user authentication required (public strategy site)
- All data is static (no sensitive information stored)
- CORS enabled for API endpoints
- SQLite database for future user management features

## 📈 Future Enhancements

- [ ] Real-time booking integration
- [ ] WhatsApp agent interface
- [ ] Customer dashboard
- [ ] Partner portal
- [ ] Analytics dashboard
- [ ] Multi-language support (Spanish)

## 🤝 Contributing

This is a proprietary project for Mr. Wright Adventures. For inquiries, please contact the development team.

## 📄 License

Proprietary - All rights reserved by Mr. Wright Adventures

## 👥 Team

**Strategy & Development**: Lenox Saint Germain  
**Business Owner**: Mr. Wright  
**Target Market**: Costa Rica Tourism (SJO & LIR airports)

## 📞 Contact

For business inquiries or partnership opportunities, please visit the deployed website or contact through official channels.

---

**Built with** ❤️ **for travelers seeking seamless Costa Rica experiences**

🌴 **Pura Vida!** 🌴
