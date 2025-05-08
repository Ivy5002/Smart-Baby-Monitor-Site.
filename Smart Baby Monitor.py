import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function SmartBabyMonitorSite() {
  return (
    <div className="p-8 space-y-16 bg-white text-gray-900">
      {/* Hero Section */}
      <section className="text-center space-y-6">
        <h1 className="text-5xl font-bold">Smart Baby Monitor</h1>
        <p className="text-lg max-w-2xl mx-auto">
          AI-powered insights for your baby's safety, sleep, and environment. Peace of mind for modern parents.
        </p>
        <Button className="text-lg px-6 py-3">Pre-order Now</Button>
      </section>

      {/* Features */}
      <section>
        <h2 className="text-3xl font-semibold text-center mb-10">Key Features</h2>
        <div className="grid md:grid-cols-3 gap-6">
          <Card><CardContent className="p-6"><h3 className="text-xl font-bold mb-2">Real-Time Alerts</h3><p>Receive instant alerts for irregular breathing, heart rate fluctuations, and hazardous room conditions.</p></CardContent></Card>
          <Card><CardContent className="p-6"><h3 className="text-xl font-bold mb-2">Smart Home Integration</h3><p>Connects with smart home systems to adjust lighting, temperature, and air quality for optimal sleep.</p></CardContent></Card>
          <Card><CardContent className="p-6"><h3 className="text-xl font-bold mb-2">Sleep Coaching</h3><p>AI-driven sleep coaching with weekly wellness reports and pattern analysis to improve sleep quality.</p></CardContent></Card>
          <Card><CardContent className="p-6"><h3 className="text-xl font-bold mb-2">Environmental Monitoring</h3><p>Detects temperature, humidity, and air quality changes, alerting you before risks arise.</p></CardContent></Card>
          <Card><CardContent className="p-6"><h3 className="text-xl font-bold mb-2">Biometric Tracking</h3><p>Monitors heart rate, breathing, and movement with precision through AI-enhanced sensors.</p></CardContent></Card>
          <Card><CardContent className="p-6"><h3 className="text-xl font-bold mb-2">Health Insights</h3><p>Weekly summaries and health tracking data to keep caregivers informed and reassured.</p></CardContent></Card>
        </div>
      </section>

      {/* Pricing */}
      <section>
        <h2 className="text-3xl font-semibold text-center mb-10">Pricing</h2>
        <div className="grid md:grid-cols-2 gap-6">
          <Card><CardContent className="p-6">
            <h3 className="text-xl font-bold mb-2">Premium</h3>
            <p>Includes AI-driven sleep coaching, environmental alerts, and wellness reports.</p>
            <p className="mt-4 font-semibold">$14.99/month</p>
          </CardContent></Card>
          <Card><CardContent className="p-6">
            <h3 className="text-xl font-bold mb-2">Elite</h3>
            <p>All Premium features plus smart home integration and pediatric consultation access.</p>
            <p className="mt-4 font-semibold">$24.99/month</p>
          </CardContent></Card>
        </div>
      </section>

      {/* Contact */}
      <section className="text-center space-y-6">
        <h2 className="text-3xl font-semibold">Contact Us</h2>
        <p className="text-lg">Have questions? Reach out to us anytime.</p>
        <form className="max-w-md mx-auto space-y-4">
          <Input placeholder="Your Email" type="email" required />
          <Input placeholder="Your Message" type="text" required />
          <Button type="submit">Send Message</Button>
        </form>
      </section>
    </div>
  );
}