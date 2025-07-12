#!/bin/bash
# TailorTalk Deployment Script

echo "🚀 Deploying TailorTalk Calendar Assistant..."

# Check if running in development or production
if [ "$REPLIT_ENVIRONMENT" = "production" ]; then
    echo "📦 Production deployment detected"
    # Production: Run both services
    python3 start.py
else
    echo "🛠️ Development deployment detected"
    # Development: Use existing workflow setup
    echo "Services should be running via Replit workflows"
    echo "Frontend: http://0.0.0.0:5000"
    echo "Backend: http://0.0.0.0:8000"
fi

echo "✅ TailorTalk deployment complete!"