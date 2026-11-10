#!/usr/bin/env python3
"""Spectral-Finance/lux#96 — Local Model Support via Ollama."""
import hashlib, json, threading, time, urllib.request
from collections import OrderedDict
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple

@dataclass(frozen=True)
class OllamaConfig:
    base_url: str = "http://127.0.0.1:11434"
    default_model: str = "llama3.2:latest"
    timeout_seconds: float = 60.0
    max_concurrency: int = 2
    cache_max_entries: int = 256
    cache_ttl_seconds: float = 300.0
    max_retries: int = 2
    retry_backoff_seconds: float = 0.25
