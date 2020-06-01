#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { GundelsbyStack } from '../lib/gundelsby-stack';

const app = new cdk.App();
new GundelsbyStack(app, 'GundelsbyStack');
