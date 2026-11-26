# v4：先允许全弧调整，再到准确保护圆弧

会话 `Astra-held10-06bbeb39-20261126`，2026-11-26。

完整数学推导见 [R70](../results/R70-full-to-complementary-phase-homotopy.md)。原v2/v3的每个phase列在保护弧内恒零，因而在所有λ上额外冻结了这段的控制曲率。原R53 support设计在λ<1仍可改变该段；两者的成败比较同时改变了入口切向空间和δ自由度，不能仅归因于固定δ。

新v4用同一完整R53零控制锚、同一g/chart/mean1168，显式改为

\[
\Psi_j^\lambda(u)=(1-\lambda)\frac{\sin(3ju)}{3j}
+\lambda\frac{W(u)\sin(\omega_jv)}{\omega_j+D_1},
\quad\omega_j=j\pi/(\pi/3-S),\ D_1=630/(256b).
\]

λ<1时保护弧内的控制曲率为 `(1-lambda)*cos(3*j*u)`；λ=1精确回到v3准确圆弧族。每列曲率上界仍为1，原更宽三阶导守卫仍有效。该设计改变中间有限族，不是把旧非零v3场换名；仅允许真正接受且全零控制的v3锚通过重新计算的原方程/两jet/metric身份转换。非零d时，λ偏导必须含 `sum(d_j*(Psi_complement-Psi_full))`；step在固定λ求原p-Jacobian，没有遗漏这项的λ方向Newton。

五件新源相对v3只作明确版本/入口族及其来源绑定扩展，原BVP、完整R48 lift、RMS/BC/metric门、固定g和mean规则均保留。已实际执行M24小检查：三档λ零控制完整F/Ft/Ftt逐位相同；12列非零控制差分最大误差3.0955843444147035e−10；λ1非零F/Ft/Ftt/phi/kappa及其两导均与v3逐位同；非零d的λ偏导差分误差≤2.7798219282004766e−10。报告见 [小检查](2026-11-26-warm-v4-contract-check.json)。这不是实际BVP接受或全局逆界。

新probe run45806625263仍先自然完成原v3一次方向诊断。其后在同runner用实际新v3零锚执行：

```text
python -u REPO/topics/visible-flex-held-10pct/scripts/resume_20261126/warm_fixed_m3_continue_v4.py --repo REPO --work WORK --source-run WORK/fresh-one-direction/v3-zero-control-anchor/run.json --outdir WORK/warm-v4-design
```

默认目标 .004/.008/.016/.032/.064/.125/.25/.5/.75/1，原mode levels 24/32/40/48/64。旧warm父链仍自然执行，未被替换或中断。当前尚无v4实际零锚转换/非零λ推进；全BVP可解性、λ1、实际fullH、闭合与同问题精化均未支付。λ1之后必须显式适配实际DN类型，不能改名当v3。

## 冻结源

- `warm_homotopy_core_factory_v4.py`：`f303897c231639b2dd68854d7bf37cc8862eea4e52b468d5be84c856e84fbcb5`。
- `warm_fixed_m3_model_v4.py`：`5eb1a30dc861747bde158315b845a62bf666c32ad1b59a033daeafe41da7fabe`。
- `warm_zero_control_reexpression_v4.py`：`fcf97b89fa361ec3215dd6e6695faefdb676aabc2a8dad1640c9d4c6d509d66d`。
- `warm_fixed_m3_step_v4.py`：`36dc28b33928e6b256308ef3481acb51ccc60e9cdcb7bb8558f197a17082706d`。
- `warm_fixed_m3_continue_v4.py`：`b8c18468635ebad021c19f0d61f6caec364ebb2343349c6345e25fa8cb2bc021`。
- `check_warm_v4_contract.py`：`dbdc4a4f163c2d88a9e3f34950f300278a76d05177df603e307262f2155fbfda`。
