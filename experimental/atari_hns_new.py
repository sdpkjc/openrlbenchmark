import wandb.apis.reports as wb  # noqa

from openrlbenchmark import Runset, plot_atari

blocks = plot_atari.plot_atari(
    [
        # Runset(
        #     name="CleanRL ppo_atari_envpool_xla_jax.py",
        #     filters=[{"config.exp_name.value": "ppo_atari_envpool_xla_jax"}],
        #     entity="openrlbenchmark",
        #     project="envpool-atari",
        #     groupby="exp_name",
        #     key_for_env_id="config.env_id.value",
        #     x_axis="global_step",
        #     y_axis="charts/avg_episodic_return",
        # ),
        # Runset(
        #     name="CleanRL ppo_atari_envpool_xla_vclip_jax.py",
        #     filters=[{"config.exp_name.value": "ppo_atari_envpool_xla_vclip_jax"}],
        #     entity="openrlbenchmark",
        #     project="envpool-atari",
        #     groupby="exp_name",
        #     key_for_env_id="config.env_id.value",
        #     x_axis="global_step",
        #     y_axis="charts/avg_episodic_return",
        # ),
        Runset(
            name="openai/baselines' PPO",
            filters=[{"config.exp_name.value": "baselines-ppo2-cnn"}],
            entity="openrlbenchmark",
            project="baselines",
            groupby="exp_name",
            key_for_env_id="config.env.value",
            x_axis="global_step",
            y_axis="charts/episodic_return",
            env_id_fn=lambda env_id: env_id.replace("-v5", "NoFrameskip-v4"),
        ),
    ],
    output_folder="static",
    return_wandb_report_blocks=True,
)
report = wb.Report(
    project="openrlbenchmark",
    entity="openrlbenchmark",
    title="openai/baselins' PPO (part 1)",
    blocks=blocks[:29],
)
report.save()
print(f"view the generated report at {report.url}")
report = wb.Report(
    project="openrlbenchmark",
    entity="openrlbenchmark",
    title="openai/baselins' PPO (part 2)",
    blocks=blocks[29:],
)
report.save()
print(f"view the generated report at {report.url}")
