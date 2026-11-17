# 同g、同923节点的唯一模态衰减三jet初猜

2026-11-17，constructive_model。原长五次桥在真实读出中有约147的 Gram 误差，角项占主导。此计划只改一次初猜生成公式；不扫参数，不增加求解预算，不改现有短 LM。

## 固定对象

保留已生成 `401255b7...` bundle 的全部 mesh、a_stages、R、S、H、width、core前三参数及有限 circle 投影。准确 Hold 标量和准确 affine-in-S 网格沿原 oracle 报告；原819个 prefix 节点的 q 三jet逐字保留。M160、923节点、1845 stage 不改。物理 lift 仍为全解析的 material circle，未截断。

旧初猜只是长物理 Hermite 桥，没有既存的完整 a/z 轴基线。此次明确新增的有限基线为

$$B(s)=a(s)C_M+[H-z_{ref}(S)+z_{ref}(s)]e_z,$$

其中 $C_M$ 是原固定8192 DFT得到的有限 circle 向量，$z_{ref}$ 是同一准确 Hold 参考高度。$B$ 的0/1/2导数分别使用准确 a/z 包围及 $a'=\sin\alpha,a''=-\kappa\cos\alpha,z'=\cos\alpha,z''=\kappa\sin\alpha$；并未另选浮点 alpha/K 初值。

## 衰减公式与接缝

令 $t=s-1,T=S-1$，固定每一旋转架模态的 $\lambda_j=\max(1,2j)/a(1)$；R/Z零模也使用 $1/a(1)$。这是固定常数，**不使用随s变动的频率**。在1处设真实三jet差为 $(dY,dU,dA)$，定义

$$p(t)=dY+(dU+\lambda dY)t+\tfrac12(dA+2\lambda dU+\lambda^2dY)t^2,$$
$$f(t)=e^{-\lambda t}p(t),\qquad\delta(t)=\zeta(t)f(t),\qquad
\zeta(t)=1-S_5(t/T).$$

全部导数按下式直接计算：

$$f'=e^{-\lambda t}(p'-\lambda p),\quad
f''=e^{-\lambda t}(p''-2\lambda p'+\lambda^2p),$$
$$\delta'=\zeta'f+\zeta f',\qquad
\delta''=\zeta''f+2\zeta'f'+\zeta f''.$$

因为 $\zeta(0)=1,\zeta'(0)=\zeta''(0)=0$，故 $(\delta,\delta',\delta'')(0)=(dY,dU,dA)$；而末端 $\zeta,\zeta',\zeta''$ 全为0，所以末端残差三jet准确为0。取节点 $q=B+\delta-L_M$ 的三jet，再与全解析 L 相加。开始节点直接保留原三jet、末节点直接置0，任何公式浮点偏差另报，保证实际保存的共享五次候选有正确 C² 接缝。

数值生成以同一 a(1) 盒中点作 rates carrier；输出的 literal binary 节点三jet才是新候选定义。没有把普通浮点评价声称为完整几何区间证书，也不继承原 M320/pulse 认证。

## 唯一执行

新 producer `parallel-model-fullclosed-mode-damped-warm.py`，8656 B，SHA256

`632d6cfc5f3113bc6f64c340fe9d066a1614c5b0bd649a357bdea2d0d94af6e8`。

固定输入是原 warm bundle `401255b7328ba2e4cdfe5af94d0a0896859960f1b474961d30aff33d8248f02a`、report `0c499334cebe74f0c417ccb89b5ee4dcf86cb07dfbab1f0d46c0b805f4a71b80`、真实原场 `26e53e8c...`、oracle `a1ed8fa5...` 及其原冻结依赖。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python "$WORK/parallel-model-fullclosed-mode-damped-warm.py" \
 --parent-bundle "$WORK/parallel-model-fullclosed-hold-warm.npz" \
 --parent-report "$WORK/parallel-model-fullclosed-hold-warm.json" \
 --input "$WORK/parallel-pulse-a5-complete-base.json.gz" \
 --scalar-source "$WORK/parallel-model-full-hold-oracle.py" \
 --integer-source "$TOPIC/notes/2026-11-17-parallel-inward-integral-enclosure.py" \
 --hold-source "$TOPIC/scripts/parallel_20261117_negative_hold_profile_ivp.py" \
 --out "$WORK/parallel-model-fullclosed-mode-damped-warm.json"
```

唯一新 bundle 完成后，geometry_amplification 用已验证的 FFT 角值算子在同1845 stage、同2048角只作一次 residual-only 读出；不重做 CS、Jv、Jᵀ 检验，不启动求解、不加密择优。实际结果不论大小都完整登记。本计划本身没有预报新 Gram 值或几何可行性。
