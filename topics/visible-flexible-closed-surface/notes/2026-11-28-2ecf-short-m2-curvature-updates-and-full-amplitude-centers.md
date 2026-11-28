# 短二次模固定度量上的大幅真实位置与主曲率更新

沿用[短母线及原生深尾定义](2026-11-28-2ecf-r262-oscillating-tail-second-mode-physical-meridian-and-shape-steps.md)的第一个 $R=1.29728266\ldots$ 新度量，在 64 个径段、每个 XYZ 坐标 8 个奇偶角通道上直接更新位置。所有表行均保持各自预定的真实中央、完整 cuff 端迹，使用同一个固定径向目标。纯二次中央幅度 $\epsilon$ 的两轴半宽差准确为 $2\epsilon$。原 .15 小帽仍限制刚体对齐后的像差，本记录没有给出完整强指标证书。

对单位主方向 $D=xX_s+yX_u$、$A=x^2X_{ss}+2xyX_{su}+y^2X_{uu}$ 和有向主曲率 $k=N\cdot A$，简单特征值的广义特征方程给

$$
\delta k= N\cdot (x^2\delta X_{ss}+2xy\delta X_{su}+y^2\delta X_{uu})+\delta N\cdot(A-kN)-2kD\cdot(x\delta X_s+y\delta X_u).
$$

其中 $\delta N=(I-NN^T)(\delta X_s\times X_u+X_s\times\delta X_u)/|X_s\times X_u|$。实际更新同时组装这个导数与三项原始度量误差导数。符号最大绝对主曲率从真实的两个主方向中选，超过 guide 的原始曲率按其物理单位保留；回溯测试实际非线性峰。固定随机位置方向在一个保存态的 184 个绝对曲率高于 6 的实际点上与中心差分相对差（分母 $1+|\delta k|$）最大 $1.65\,10^{-9}$。该检验属于浮点观察。

| 中央与实验 | 接受步 | 917×225 移位度量峰 | 移位曲率峰 | 17046×120 独立原生深表曲率峰 |
|---|---:|---:|---:|---:|
| 纯二次 $\epsilon=1/8$ | 20 | .01063323 | 9.80987 | 9.74345 |
| 纯二次 $3/16$ | 26 | .02767304 | 10.24498 | 12.21335 |
| 纯二次 $1/4$ | 26 | .06326859 | 10.29069 | 13.66266 |
| 纯二次 $.34$ | 32 | .14371051 | 10.66851 | 16.07949 |
| 纯二次 $.38$ | 32 | .19445877 | 10.83236 | 17.12401 |
| 纯二次 $1/4$，深表峰纳入求解 | 28 | .06477065 | 10.06517 | 10.25687 |
| 纯二次 $.34$，深表峰纳入求解 | 23 | .11259148 | 12.22159 | 12.61369 |
| 平滑支撑 $.34$，深表峰纳入求解 | 12 | .11017922 | 13.07617 | 12.59349 |

普通独立观察外，每组另有 926×192 网格，末列另覆盖有限表的全部原生径行。最后三组沿每个原 profile 的准确物理标签作 48 角整表筛选，把局部最大的原始度量和曲率行加入实际微分系统，每五次接受后刷新。原来的两套普通网格在中、大幅状态确实漏掉较深的曲率尖点。补点后 $1/4$ 的普通度量稍回升，深部曲率从 13.66266 降至 10.25687。$.34$ 的常规曲率稍回升。误差和 reach 强门仍未完成。

平滑支撑按 $p=32$、$j=1,\ldots,p$ 定义 $c_j=2(-1)^j\binom{2p}{p-j}/\binom{2p}{p}$、$b_j=c_j/(1-4j^2)$、$D_*=\sum_{j\ \mathrm{odd}}b_j>0$，$h(\varphi)=R+(\epsilon/D_*)\sum b_j\cos(2j\varphi)$。于是 $h(0)-h(\pi/2)=2\epsilon$ 且 $h+h''=R+(\epsilon/D_*)[\sin^{2p}\varphi/\langle\sin^{2p}\rangle-1]$。由正下界 $R-\epsilon/D_*$ 可反演真实周期弧长，保持周长 $2\pi R$。$.34$ 输入的两个半宽为 1.56792604/.88792604，曲率峰约 1.23014，较纯二次中央更平。真实移位采样的核点最大欧氏范数为 1.56792604，纯二次 $.34$ 则为 1.63728266。以两倍采样最大范数作直径估计的观察只涉及实际采样核，不能支付连续整闭直径和非局部 reach。

使用[同一父数据再生记录](2026-11-28-2ecf-r262-oscillating-tail-second-mode-physical-meridian-and-shape-steps.md)中的 `S`、`W`、`b` 参数数组及单线程 BLAS。

```bash
k=2ecf-r262-m2-physical-curvature-response.py
n=2ecf-r262-m2-deep-active-curvature-response.py
h=2ecf-r262-m2-stadium-deep-physical-response.py
act() { local solver=$1 parent=$2 out=$3 epsilon=$4 steps=$5 mu=$6 guide=$7; shift 7; python "$S/$solver" "${b[@]}" --parent "$W/$parent.json" --out "$W/$out.json" --epsilon "$epsilon" --steps "$steps" --mu "$mu" --guide "$guide" "$@"; }
q=g12-m2-physical-curvature-eps
v=g12-m2-deep-active-curvature-eps
act "$k" g12-m2-physical-eps1over8-nested64 "${q}1over8" .125 20 .018 9.65
act "$k" "${q}1over8" "${q}3over16" .1875 26 .018 9.65
act "$k" "${q}1over8" "${q}1over4" .25 26 .035 9.65
act "$k" "${q}1over4" "${q}034" .34 32 .045 9.4
act "$k" "${q}1over4" "${q}038" .38 32 .06 9.3
act "$n" "${q}1over4" "${v}1over4" .25 28 .055 9.4
act "$n" "${q}034" "${v}034" .34 35 .055 9.4
act "$h" "${v}034" g12-m2-stadium-deep-curvature-eps034 .34 28 .047 9.4 --stadium-p 32 --stadium-mix 1
```

| 源码或产物 | SHA-256 |
|---|---|
| `2ecf-r262-m2-physical-curvature-response.py` | `0590e1d68d0abccf88b98ff303607e5a53ae9c28835b335a52e239fc03389435` |
| `2ecf-r262-m2-deep-active-curvature-response.py` | `0accc740248fc05cf8566d0c99464fddcca98a4f085b8a8804a1d4ca0438f55d` |
| `2ecf-r262-m2-stadium-deep-physical-response.py` | `f8180602d999e74bf8379bc101d483eba033831502e3aecbb0c5bb92eda582a4` |
| `g12-m2-deep-active-curvature-eps034.json` | `b27b6faa453b0bb04dc1519cc6278b9d5ba63ad1977c3c09e328fff1a75884ed` |
| `g12-m2-deep-active-curvature-eps1over4.json` | `f113fce5c1c186e2ce2b8a8469846b15bf54588784738e4e22a209767b227c69` |
| `g12-m2-physical-curvature-eps034.json` | `f2f738ab4e3f19b38c7fc0df836ad519d4377222f72222c6c70aafaa6a770807` |
| `g12-m2-physical-curvature-eps038.json` | `16df05820ff9553988b3b82d9fde589e18a95f6628efac335d2b1aee9b45220f` |
| `g12-m2-physical-curvature-eps1over4.json` | `8616d7a2fcdb185c6358796811c5e601d71e5eedd4df7fc0a9fc283c5a8a13f6` |
| `g12-m2-physical-curvature-eps1over8.json` | `671cb109ed72e7f1d6585721fcd0c6d35b735ce367f8c36f712a5340ffea4046` |
| `g12-m2-physical-curvature-eps3over16.json` | `45be6059c0d1e929967e4d74c882a62467c9ee6db47652b899981958cbf18bfc` |
| `g12-m2-stadium-deep-curvature-eps034.json` | `64ee719b1faeafc12f1791d43bb1254c37386113fa9031ce0f7dd6de639d29a5` |
