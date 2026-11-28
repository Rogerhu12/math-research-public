# R80 — 实际完整 full-H 尾的绝对位置、支撑和曲率

维护：Astra-held10-7c4e33ee-20261128 / tail_closure，2026-11-28。

**已证明并实际执行：** 对当前原 λ=.002/M24/N512 full-H 的同一完整有限尾场，采用实际宽度 .12 的 prefix cut 证书所固定的竖向原点，全部 1152 个 stage、18,460 个原径向 spans、同一深端零 jet collar 和平盘满足

$$\boxed{|F|\le0.9204371195066212,\qquad
F\cdot n\ge0.7710414327607057,\qquad
|\kappa_i|\le10.017503096013616.}$$

十进制均向外舍入；原输出保存 exact rational 界。结果对全部角度、全部相位及上下反射同时成立。这里中央柱半长为 0、marker 为 0；正短柱和 R67 三重帽的成本仍须另付。本条不声称完整尾 metric 已通过，也不声称整个闭族、同 g 收敛或握持完成标准。

## 1. 实际竖向原点，未借用 query 近似数

独立入口 `scripts/resume_20261128/tail/tail_actual_placement.py` 先验证同一真实完整 bundle、full raw-H factor 1、源 run、全部物理参数、相同 literal prefix jets、.12 cut 的完整源/数据身份，以及已经实际证明的 $c=R_c$ 半径恒等。没有把 raw-H 与后续 coupled physical-H 混用。

从原前缀定义数组的实际零模读取

$$z_{\rm cut}=\frac{7630983381811369}{9007199254740992}.$$

complete Cartesian 构造的零模节点由原 mean spline 在相同节点取值定义；cut 端 exact-core lift 和 phase chart 的全部二阶 jet 都为零。该字面零模与 .12 cut 的同一精确 target 定义相等。

从完整原 mean chain 和 stage 0 公共节点读出同一个字面值 $\mu_{\rm cut}$，逐字面核对它与完整 height 零模系数相等，定义

$$z_b=z_{\rm cut}+\mu_{\rm cut}.$$

随后使用**同一 R58 真实定义**的已证 normalization 与完整 height 积分，包括内端深尾余项，

$$H_*:=\int_{a_0}^{R_c}w(R)\,dR
\in\left[\frac{3281804030831981}{144115188075855872},
\frac{820451008699367}{36028797018963968}\right].$$

原 `validate_inputs` 重核该归一化证书与相同原证明记录、全部校准常数、源 SHA 和真实背景 definition SHA。原 primitive 在 cut 上的半径及零 height drop 也实际核过。没有重算已证明的积分，没有用 JS profile 或查询器显示值定义高度。

于是平盘高度的真区间为

$$Z_{\rm cap}=z_b+H_*\in
[0.8699871644491405,\ 0.8699871644766567].$$

完整上尾是

$$F=X_0+V,\qquad
X_0(R,\theta)=\left(R e_r(\theta),\ z_b+H_*-h(R)\right),$$

其中 $h(R)=\int_{a_0}^R w$，$V$ 的高度分量为原完整 mean/Fourier 扰动的负号。因此在 cut 上相同 $\mu_{\rm cut}$ 精确抵消，竖向 mean 没有重复叠加，也没有重置任何段的 mean。

## 2. 真实背景的绝对半径和支撑界

R58 同一背景已有 $0\le w\le41/100$。因 $h$ 单调、$R\le R_c$，上尾背景满足

$$z_b\le (X_0)_z\le z_b+H_*^{\rm up},\qquad
|X_0|\le\rho_0:=\sqrt{R_c^2+(z_b+H_*^{\rm up})^2}.$$

外法向为

$$n_0=\frac{(w e_r,1)}{\sqrt{1+w^2}},\qquad
X_0\cdot n_0
=\frac{Rw+(X_0)_z}{\sqrt{1+w^2}}
\ge s_0:=\frac{z_b}{\sqrt{1+(41/100)^2}}.$$

用精确有理算术和向上平方根分别取得

$$\rho_0\le0.9202595646632168,\qquad
s_0\ge0.783887361770741.$$

这是实际高度给出的绝对界，未使用原宽窗 $z_b\in[.1,1.28]$ 中较弱的 $1/11$ 支撑下界。

## 3. 只复用原已证几何，完整支付扰动

原 full-H 全尾几何运行已经真实结束，所有 stage 与新深 collar 的证书都保留原哈希。本入口逐项重核对应 stage 的完整 spectrum/status/parameters、实际文件 SHA、mapHash、原 span 数与所引用原证书。没有重算已付一阶、二阶或曲率多项式。

设某个实际组件的原证书给出归一一阶扰动界 $\eta<1$、位置扰动界 $p\ge0$。在背景正交切标架中，交叉积扰动不超过

$$c=\sqrt2\,\eta+\tfrac12\eta^2.$$

原法向引理给出

$$\|n-n_0\|\le N(\eta):=
\min\left(2,\frac{2c}{1-c}\right),\qquad c<1.$$

所以同一组件上严格有

$$|F|\le\rho_0+p,\qquad
F\cdot n\ge s_0-\rho_0N(\eta)-p.$$

这里使用 $|n|=1$，因而无需额外 $pN(\eta)$ 项。整体竖向反射保留 $\eta,p$ 及主曲率绝对值；相位作用是旋转并重标角度，上下反射亦保留这些标量界。法向连续定向与上 cut 一致。

对全部 1152 个 stage、同一实际 deep collar 和内侧旋转 cuff/平盘逐项支付上述界，再取全局最值，得到开头三项结果。原 deep collar 的公共外端二阶 jet、内端零二阶 jet 和完整 mean 身份均重新绑定；内侧旋转组件使用同一 R58 的 $K\le8$，没有漏掉深尾。

曲率直接采用同场原有效上界。stage 82 的原内部 $K<10$ allocation 仍为 false；其严格上界 $10.017503096013616$ 本身已经满足全局 $K<123/10$。本入口明确保留原 false，不更改原证书或门。

## 4. 真实执行与范围

TTY 42675 实际 exit 0，summary SHA 为 `b001a374546aaad59ed3167a12d6ae2233e91f0429e70b421235f1ee53c24d2e`。完整入口参数、数学源、cut/source/mean/normalization/radius identity 和全部输出哈希见[小结果](../notes/2026-11-28-tail-actual-absolute-placement.json)。1154 个组件行只留 scratch，不入 Git。

报告 245.89018336899971 秒包含等待原末段几何证书的时间，未单独测纯计算时长。原积分与原几何多项式均没有重算。

这付清当前未加柱、未加帽的实际尾盘绝对几何预算，并与实际 .12 cut 的源/原点一致。完整相对 metric 的独立同场 Taylor 补充仍在继续；精确 λ1 握持结构、后续 fixed-g 精化和完整课题完成标准没有由此获得。

## 5. 连续证明的复现入口

运行 `scripts/resume_20261128/tail/tail_actual_placement.py`，全部 CLI 值逐项给在上引 JSON 的 `cli`；两项 `--original-summary` 都必须保留。输入是原真实 source run、完整 geometry bundle、R79 cut、已付真实背景 normalization 和全尾半径恒等。只重用同一已付界，不能把其它 λ、mean 或 physical-H 的结果放入此入口。全原几何终态及其深盘接缝/投影单射证明另见 [原执行记录](../notes/2026-11-28-tail-original-full-geometry-terminal.md)。
