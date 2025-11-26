def load_parameters():
    # Minimal parameters for a smoke test. These are safe defaults and may be
    # overridden by the project's normal config when running for real.
    return {
        'train_data': 'both',
        'use_hidden_layer': False,
        'dropout': 0.5,
        'max_lr': 1e-3,
        'weight_decay': 0,
        'use_lr_scheduler': False,
        'n_epochs': 1,
        'pct_start': 0.3,
        'batch_size': 4,
        'sample_ratio': 0.01
    }


def set_tag(tag):
    print(f"[foundations] set_tag: {tag}")


def log_params(params):
    print(f"[foundations] params: {params}")
