import React from 'react';
import { Link } from 'react-router-dom';
import { Brain } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-[#0a0a0a] border-t border-gray-800 mt-auto">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <Brain className="w-6 h-6 text-cyan-400" />
            <span className="text-lg font-bold bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
              Digital Twin
            </span>
          </div>

          <div className="flex items-center gap-6 text-sm text-gray-400">
            <Link to="/privacy" className="hover:text-cyan-400 transition-colors duration-200">
              Privacy Policy
            </Link>
            <Link to="/terms" className="hover:text-cyan-400 transition-colors duration-200">
              Terms of Service
            </Link>
          </div>

          <p className="text-sm text-gray-500">
            © 2026 Digital Twin. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;