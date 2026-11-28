# 两个新 Γ95 的同角四阶母线与整环带数据

[R283](../results/R283-nonelliptic-accurate-rulings-global-reach.md) 用 R281 p8 的原 v=.045 数据和 p32 r=1/4 的新 v=.012 数据。两套真实 Γ95 SHA 分别为 `8672f468f460293976d2474c1bd52bd092d8f5c0f006709335c1a18fc055f244` 与 `978458636447335c6e00d542fdac538c5f27975b95ae92d56cc65d17ba6af502`。分别按[R281 原生再生](2026-11-28-2ecf-strong-positive-stadium-H65-native-ramp.md)与[新坡度输入](2026-11-28-2ecf-stadium-full-gap-H65-slope-physical-inputs.md)生成。Gamma 的全部存储 Fourier 模都按其二进分数参与，$f_0$ 取相应 coast 文件的真实正半径。这里不需要把原生 ODE 数值轨迹认作无限维准确解。

同角程序使用 96 位有向整数算术。每个基盒上的实际 $k,k_t,n,K$ 共用同一空间曲线 Taylor 变量，保留全部非线性分式、开方、角导数。正平方根或分母不定以及超过指定分辨目标时细分。1024 个全圈基盒含完整端点；归一均速先取独立有向中点求积上、下界。对每个 $L$ 从 $0$ 到整个 $L$ 用 $[0,w(L)]$ 输入母线分母和主曲率。另用 2048 个闭角盒证明真实入口投影切向度数、投影曲率和空间弧长相对投影的因子。所有表中 reach 的弦长预算由有理数核验；$\arcsin$ 上界使用 $\sin t\ge t-t^3/6+t^5/120-t^7/5040$ 和 $t<\pi/2$。原两个程序、全部四个实际进程自然退出 0。未提交可重算的全角数组。

```bash
for spec in '8 stadium-p8A145-H65' '32 stadium-p32r25-v012-H65'; do
  read -r p input <<< "$spec"
  python "$S/2ecf-strong-stadium-correlated-ruling-interval.py" --scripts "$S" --input "$input.json" --coast "$input-coast.npz" --output "stadium-p$p-coast-tight.json" --cells 1024 --extend .06 .10 --curvature-target 9.45
  python "$S/2ecf-strong-stadium-coast-global-reach.py" --scripts "$S" --coast "$input-coast.npz" --certificate "stadium-p$p-coast-tight.json" --output "stadium-p$p-coast-reach.json" --cells 2048
done
```

源码 SHA-256 分别为 `612d6ffea6c5f412112913868e29045caebab7cca99c10f7af86ff6a61d8496b`、`f88828f3b4fb2e608c87db4eeeeadaf69c1daa22a93337d63fffa4c046057da2`。p8 实际四阶母线与 reach 回执为 `f982018b3f9d8f681fe45aaa316a8855ee6e597ba1d7409dd22cd307235ae82a`、`ecea0920125005d9f5f1176ff6e315b26d94bdfd325baeae5ba17954431f89e9`。p32 两份依序为 `e602ab44b70ada8621cc80f17c688c4da2a844d994c92e3ba2c6687784d7fc2f`、`8f1ac756b420ce9b217381bf13e39fbe10257883a981c9cbda9bfb549d286445`。含实际运行时间的 JSON 每次写出时其整体 SHA 可能变化，数值不等式不依赖计时。
