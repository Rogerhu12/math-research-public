# M24 真核心前缀的精确 C² 圆柱入口修补

维护会话：Astra-held10-1b6d88ec-20261120。

**状态：已证明（实际执行的连续区间证书）。** 对 `newg-wide-lambda0p002-m24-linear` 所定义的当前真核心、共同 Hermite 前缀，构造一个仅作用于 $0\le s\le L=1/1000$ 的新图 $\widetilde F$。它在 $s=0$ 与真 R53 核心圆柱

$$
 C(s,\theta)=\Gamma(\theta)+s e_z
\tag{1}
$$

精确共享全部 Cartesian 二 jet，在 $s=L$ 与原图精确共享全部二 jet。原物理场、旧源码和段外图均未改动；目标材料度量仍为同一个 $g=ds^2+a(s)^2d\theta^2$。

本次局部证书给出

$$
 \|g^{-1/2}(\widetilde F^*e-g)g^{-1/2}\|_{\rm op}
 <8.199\times10^{-7},\qquad
 |\kappa_i(\widetilde F)|<2.185,
\tag{2}
$$

以及半径 $<1.14$、支撑函数 $>0.504$。这些结论只支付当前单张近似前缀的真实中央入口，不证明最终 $\lambda=1$、闭面存在或同 $g$ 精化收敛。

## 1. 固定的图和坐标

使用同一 `run.json` 和 `physical.npz`，SHA-256 分别为

```
c44b6fd2fbb13cc9ce0451cc6ab1d3c06521de0622de27190bde94c4c550462a
f2e22fe19bb0b6fdeff79c4fa99363d9be6cbb1ef382fd882679a2b717a3030d
```

$\Gamma$ 是 [真 R53 积分核心](2026-11-20-m24-r53-true-core-jet-certificate.md)，不是浮点缓存曲线。原图是 [共同 Hermite 场、端点归一 profile 和固定 1168 点真均值原函数](2026-11-20-m24-prefix-absolute-height-certificate.md) 定义的 $C^2$ 图，其完整位置公式、参数绑定和连续位置／支撑界见 [前缀位置证书](2026-11-20-m24-prefix-continuous-position-support.md)。

保持原材料角 $\theta$。计算角图仅用于求值：

$$
 \theta=\psi-\frac{e(s)}3\sin3\psi,\quad
 \rho=1-e(s)\cos3\psi>0,\quad
 v=-\frac{e'(s)\sin3\psi}{3\rho},\quad
 \partial_s\big|_\theta=\partial_s\big|_\psi-v\partial_\psi.
\tag{3}
$$

本修补没有把 $e(0)$ 偷换成用于定义 lift 的 `warp_e`，也没有重置均值或高度。所有边界差都按 (3) 转到固定材料坐标后修正。

令 $G=q\mathcal B(Y)$，$H(\psi)=\Gamma(\theta_w)-e_r(\theta_w)-q\mathcal B(I)$，其中 $\theta_w=\psi-w\sin3\psi/3$、$w=\texttt{warp_e}$，$I$ 是原冻结投影。本图为

$$
 F=a e_r(\theta)+G+a\chi H+Z e_z,
 \qquad Z'=M_{1168},\quad Z(0)=0.
\tag{4}
$$

精确有理端点检查给出 $a(0)=\chi(0)=1$，$a'(0)=a''(0)=\chi'(0)=\chi''(0)=0$，$e'(0)=0$。但保存的 $Y(0)-I$、$Y_s(0)$ 并非字面为零，且

$$
 e(0)-w=\frac{1080863910568919}{10141204801825835211973625643008},
\quad
 e''(0)=-\frac{274298266965483714477266344585}{20117949056089829906655254472}.
\tag{5}
$$

因此不能仅凭“exact lift”名称宣布 (1) 的精确接缝。

## 2. 真实材料入口差的连续证书

定义实际差函数

$$
 \Delta_0(\theta)=F(0,\theta)-\Gamma(\theta),\quad
 \Delta_1(\theta)=F_s(0,\theta)-e_z,\quad
 \Delta_2(\theta)=F_{ss}(0,\theta).
\tag{6}
$$

以 $e_0=e(0)$、$\rho_0=1-e_0\cos3\psi$ 表示，(4) 的材料求导和端点恒等式给出

$$
 \Delta_1=q\mathcal B(Y_s(0))+(M_{1168}(0)-1)e_z,
\tag{7}
$$

$$
 \Delta_2=q\mathcal B(Y_{ss}(0))+M'_{1168}(0)e_z
 -v_s(0,\psi)\big(q\mathcal B(Y(0))_\psi+H_\psi\big),
 \quad v_s(0,\psi)=-\frac{e''(0)\sin3\psi}{3\rho_0}.
\tag{8}
$$

式 (8) 保留了角图加速度的完整对流项。仅 $q\mathcal B(Y_{ss}(0))$ 的系数范数约为 $.803$，相消后才得到下面的小界。

为严谨支付 $e_0-w$，令 $J=\Gamma-e_r$，将 $\psi$ 看成入口材料角的函数，并置 $d(\theta)=(e_0-w)\sin3\psi(\theta)/3$。则

$$
 \Delta_0=J(\theta+d)-J(\theta)+q\mathcal B(Y(0)-I)(\psi(\theta)).
\tag{9}
$$

既有真核心证书给出 $|J'|\le2$、$|J''|<3$、$|J'''|<6.3$。由 $\rho_0>1/2$ 和

$$
 |d|\le|e_0-w|/3,\quad
 |d_\theta|\le|e_0-w|/\inf\rho_0,\quad
 |d_{\theta\theta}|\le3|e_0-w|/(\inf\rho_0)^3
$$

可用均值定理包住 (9) 的前两阶材料角导数；剩下有限 Fourier 部分以精确有理系数范数包围。旋转径向／切向基的第 $k$ 阶 Cartesian 导数使用 $(m+1)^k$，竖向基使用 $m^k$。

式 (8) 在已认证的 4672 个真核心节点上相消，再以同一批闭角盒的 $\partial_\psi^2\Delta_2$ 范数包围支付线性插值余项。向量版本的 Green 核公式给出每个角间隔上

$$
 \sup|\Delta_2|\le\max_{\rm nodes}|\Delta_2|
       +\frac{h^2}{8}\sup|\partial_\psi^2\Delta_2|.
\tag{10}
$$

末间隔覆盖真 $2\pi$，端点值由周期性复用角零。材料角导数按 $\partial_\theta=\rho_0^{-1}\partial_\psi$ 转换。均值 $M_{1168}(0),M'_{1168}(0)$ 使用同一个完整 lift 和已认证 1168 个核心节点，只计算这次所需的入口，未重做完整均值积分。

实际执行得到以下全角范数上界：

| 函数 | 零阶 | 一阶材料角导数 | 二阶材料角导数 |
|---|---:|---:|---:|
| $\Delta_0$ | $1.630270884218238\,10^{-14}$ | $1.0307383306923116\,10^{-13}$ | $3.4621197788343905\,10^{-12}$ |
| $\Delta_1$ | $6.22142613464715\,10^{-13}$ | $9.526789100462328\,10^{-13}$ | $1.1923253436362194\,10^{-10}$ |
| $\Delta_2$ | $8.208334175024687\,10^{-7}$ | $.21875346722727812$ | $4.2320064910853095$ |

$\Delta_2$ 节点范数上界 $5.39608263512818\,10^{-7}$，插值余项 $2.8122515398965056\,10^{-7}$；后两列有意保留粗而严格的角盒范围。另有

$$
 M_{1168}(0)\in[.9999999999993874,1.0000000000006133],
\quad
 M'_{1168}(0)\in[-3.2163545463384634,3.2163545357439393]10^{-18}.
\tag{11}
$$

这些均为范围上界，不把非零上界误写成某个误差的严格正下界。

## 3. 明确的新图与精确两端二 jet

对 $0\le u\le1$ 定义

$$
\begin{aligned}
 h_0(u)&=1-10u^3+15u^4-6u^5,\\
 h_1(u)&=u-6u^3+8u^4-3u^5,\\
 h_2(u)&=\tfrac12u^2-\tfrac32u^3+\tfrac32u^4-\tfrac12u^5.
\end{aligned}
$$

取 $A_j(s)=L^j h_j(s/L)$，$L=1/1000$；在 $s\ge L$ 令 $A_j=0$。新图定义为

$$
 \widetilde F(s,\theta)=F(s,\theta)-\sum_{j=0}^2A_j(s)\Delta_j(\theta).
\tag{12}
$$

精确有理多项式恒等式为

$$
 A_j^{(k)}(0)=\delta_{jk},\qquad
 A_j^{(k)}(L)=0\quad(0\le j,k\le2).
\tag{13}
$$

代入 (6) 立即得 $\widetilde F(0,\theta)=\Gamma(\theta)$、$\widetilde F_s(0,\theta)=e_z$、$\widetilde F_{ss}(0,\theta)=0$。对这些恒等式再作材料角求导，支付位置角导数、混合导数和二阶角导数，因此全部 Cartesian 二 jet 与 (1) 相同。在 $s=L$，(13) 支付与旧图的全部二 jet。$\Delta_j$ 具有所需的连续材料角二导数，故 (12) 是明确的 $C^2$ 图。

这一步修掉入口的实际保存场差、角图起值差、非零速度误差和完整加速度缺陷；没有把这些差悄悄归零。作为新表示，(12) 可以直接延拓到 $s\le0$ 的真核心圆柱。由于 $a(0)=1,a'(0)=a''(0)=0$，两侧目标度量也以共同二 jet 接合。此处圆柱核心仍是当前 $\lambda=.002$ 的 $\Gamma$，不能把它改称最终保护圆弧核心。

原来的 $M_{1168}$ 及其真原函数保持为 (4) 的固定输入；(12) 的显式修正可以包含竖向零模。故这不是重新选择均值规则，却也不声称新图在补丁内仍满足旧 Frenet 均值演化方程。它是对该固定输入图作的已支付局部几何修正，且在 $s\ge L$ 连位置与高度都原样恢复。

脚本同时提供 `apply_material_patch(base,inlet,s,length)`，对完整材料坐标位置／二 jet 应用 (12)。其中 `inlet[j][k]` 明确是同一完整图的 $\partial_\theta^k\Delta_j$；有限求值器不自行证明浮点舍入，连续证明使用下述范围运算。

## 4. 只在修补段重付度量和曲率

把 $[0,L]$ 按原共同 Hermite、profile 和角图节点分成 5 片。每片对 $A_j$ 及其前两阶导数使用精确有理 Bernstein 范围；profile 的同一范围计算给出 $a\ge1$。

记 $P=\widetilde F-F$，由第 2 节的 $d_{jk}\ge\|\partial_\theta^k\Delta_j\|_\infty$ 得

$$
 \|P_s\|\le\sum_j|A_j'|d_{j0}=b_s,\qquad
 \|P_\theta/a\|\le\sum_j|A_j|d_{j1}/\inf a=b_\theta.
$$

令 $d=(b_s^2+b_\theta^2)^{1/2}$。原图的相对 Gram 矩阵在**同一局部片**重新用真核心、固定均值、径向 Taylor 与全角插值认证，得到 $\varepsilon_{\rm loc}$。因此

$$
 \varepsilon_{\rm new}\le\varepsilon_{\rm loc}
       +2\sqrt{1+\varepsilon_{\rm loc}}d+d^2.
\tag{14}
$$

这里没有用完整前缀最坏误差替代局部值，也没有重新定义 $g$。实际最坏旧局部上界为 $8.118627729214759\,10^{-7}$，修补后为 $8.198628090604838\,10^{-7}$。

曲率直接使用同一新图的一／二 jet：在归一目标标架 $(\partial_s,a^{-1}\partial_\theta)$ 中，向旧 $F_{ss},F_{s\theta}/a,F_{\theta\theta}/a^2$ 加入由 $A_j'',A_j',A_j$ 及 $d_{j0},d_{j1},d_{j2}$ 给出的完整修正范围；新单位法线由新的一阶列叉积归一化得到。对新第二基本形式作对称算子范围，再除以 $1-\varepsilon_{\rm new}$，即包住两个实际主曲率的绝对值。没有把旧曲率值当作新曲率。

位置／支撑传播只用已经完成的同图连续范围。若旧局部度量误差为 $\varepsilon_{\rm loc}$，其最小切向奇异值至少 $\sqrt{1-\varepsilon_{\rm loc}}$。沿旧图到新图的连续线段，$d$ 小于该值，故取向一致，且

$$
 |\widetilde n-n|\le\sqrt2\,d/\sqrt{1-\varepsilon_{\rm loc}}.
\tag{15}
$$

于是 $|\widetilde F|\le|F|+|P|$，$\widetilde F\cdot\widetilde n\ge F\cdot n-|F||\widetilde n-n|-|P|$。本次实测证书范围如下：

| 量 | 连续上／下界 |
|---|---:|
| 修补段相对度量算子范数 | $\le8.198628090604838\,10^{-7}$ |
| 修补段主曲率绝对值 | $\le2.184207126065487$ |
| $\sup|P|$ | $\le2.8843487522495366\,10^{-14}$ |
| 归一一 jet 差 | $\le4.000016437771917\,10^{-9}$ |
| 单位法线差 | $\le5.656879792317889\,10^{-9}$ |
| 新半径 | $\le1.1393302427229688$ |
| 新支撑函数 | $\ge.504183075876027$ |

5 片全部通过，0 次额外分裂；4672 个闭角盒覆盖全部角周期。段外 (12) 与原图字面相同，故原段外证书可直接复用，不能借本局部结论宣称尚未完成的段外度量门已通过。

## 5. 源、实际执行及复现

本地入口证书进程 `53097`、补丁证书进程 `65611` 均实际 `exit 0`。分别耗时 38.2522 秒、76.2901 秒。最早入口程序在“平方和区间下端因向下舍入略低于零”的平方根保护处退出；修正为与已知 $[0,\infty)$ 相交后按同一数学对象执行成功，未改变输入、门或结论。

| 内容 | SHA-256 |
|---|---|
| `certify_m24_cylinder_inlet_jets.py` | `8c52fa241fa8c42f3fb2d8656843f4038485cf723bcbf082d6e44017c8542720` |
| 入口完整执行输出 | `91f819b0d0da78ad974a0a2815aece0e4f26b9b9af5119c84055e89a7b938cd6` |
| `certify_m24_material_cylinder_patch.py` | `2ea54f16fb7c2619a8b08fbb8193b794adec86dd637930b088582d4b06e8caa9` |
| 补丁完整执行输出 | `fa601e8534a7480b369cd5c07f3f04ddeb259f785b6e30159f55e49c38103acf` |

两脚本位于 `scripts/resume_m3/`。原度量核 SHA-256 为 `6b36ccd6bab54fa35c6fe62a433f417faf7a51b80c35b798b17567eb22714986`；共同前缀库为 `1a0a45db78a9aa62884459a6542d20f6995ea152962030919fbbb74d8aee573e`。真核心和位置输入的完整生成参数／散列见第 1 节引用；数组和完整执行 JSON 留在 scratch，不入库或 Release。

在本课题目录执行，令 `$WORK` 指运行数据父目录；公共参数文件或命令行须分别提供 `--source-run`、`--physical`、`--core-mean-intervals`、`--core-mean-certificate`、`--core-angle-intervals`、`--core-angle-certificate`、`--interval-kernel`、`--support-dir` 和 `--out`。本次固定路径对应

```
$WORK/m3-work/newg-wide-lambda0p002-m24-linear/{run.json,physical.npz}
$WORK/geometry-work/newg-m24-r53-core1168-{intervals.npz,certificate.json}
$WORK/geometry-work/newg-m24-r53-core4672-{angles.npz,angles.json}
scripts/finite_closure/m3_m8_closed_map/interval_geometry_kernel.py
scripts/resume_m3
```

先运行 `certify_m24_cylinder_inlet_jets.py`，输出 `m24-cylinder-inlet-jet-certificate.json`；再用相同参数运行 `certify_m24_material_cylinder_patch.py`，增加

```bash
--inlet-certificate "$WORK/geometry-work/m24-cylinder-inlet-jet-certificate.json" \
--position-certificate "$WORK/geometry-work/newg-m24-prefix-position-support.json" \
--length 1/1000 \
--out "$WORK/geometry-work/m24-cylinder-patch-certificate.json"
```

本次可直接复现的完整命令（先前核心／位置输入按相应记录生成）：

~~~bash
WORK=/workspace/scratch/1b6d88ecddf3
TOPIC="$WORK/math-research-public/topics/visible-flex-held-10pct"
common=(
  --source-run "$WORK/m3-work/newg-wide-lambda0p002-m24-linear/run.json"
  --physical "$WORK/m3-work/newg-wide-lambda0p002-m24-linear/physical.npz"
  --core-mean-intervals "$WORK/geometry-work/newg-m24-r53-core1168-intervals.npz"
  --core-mean-certificate "$WORK/geometry-work/newg-m24-r53-core1168-certificate.json"
  --core-angle-intervals "$WORK/geometry-work/newg-m24-r53-core4672-angles.npz"
  --core-angle-certificate "$WORK/geometry-work/newg-m24-r53-core4672-angles.json"
  --interval-kernel "$TOPIC/scripts/finite_closure/m3_m8_closed_map/interval_geometry_kernel.py"
  --support-dir "$TOPIC/scripts/resume_m3"
)
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_m3/certify_m24_cylinder_inlet_jets.py" "${common[@]}" \
  --out "$WORK/geometry-work/m24-cylinder-inlet-jet-certificate.json"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -u \
  "$TOPIC/scripts/resume_m3/certify_m24_material_cylinder_patch.py" "${common[@]}" \
  --inlet-certificate "$WORK/geometry-work/m24-cylinder-inlet-jet-certificate.json" \
  --position-certificate "$WORK/geometry-work/newg-m24-prefix-position-support.json" \
  --length 1/1000 --out "$WORK/geometry-work/m24-cylinder-patch-certificate.json"
~~~

[精简实际执行记录](2026-11-20-m24-cylinder-inlet-execution.json)保留全部来源哈希与最终标量，不含可再生场数组。

## 6. 尚不推出的结论

修补定义保持目标 $g$，但本次只认证一个有限表示的近似图。它不会把该近似图变成精确等距解，也不会证明未来固定全部参数的网格／频率精化使误差趋零。后续若真非线性尾联立改变物理场，必须对新输入重新核真实入口并绑定此表示。前缀—桥、桥—尾以及最终闭合帽的共同两 jet 仍按各自实际对象支付；不能从这个中央接缝推断其他接缝自动成立。
