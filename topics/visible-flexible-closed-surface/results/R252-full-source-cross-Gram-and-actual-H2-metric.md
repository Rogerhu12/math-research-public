# R252：原 M12 完整交叉 Gram 抵消与首个真实 H2 场的全域度量证书

## 结论与范围

对本会话实际保存的首个 H2 直接 LM 场

`b6425243454a6a019d06a729405b0ebdaa0dbbc68b73b7f62745b1587174be1c`

保持原 M12 的同一个 g、原 X+C 源、同一全部角通道、同一 central/true cuff 两 jets，完整覆盖原 487 个样条区间及所有角度，得到

\[
\boxed{\ \|g^{-1/2}(Y^*\delta-g)g^{-1/2}\|_{\rm op}
\le \frac{39610910687186272171317}{39614081257132168796771975168}
<10^{-6}.\ }
\]

显示值为 \(9.999199635623173\times10^{-7}\)。严格比较采用所列准确有理数，不采用显示舍入。这里 \(Y=X+C+W\) 是同一个实际场，不加 R250 的 Q，不重定义 g，也不重新拟合 W。

完整消费自然退出 0，用时 156.746072373 秒。原 487 元被覆盖为 506 个准确 Bernstein 子片：158 个用原 R236 局部转移覆盖前缀及极近交界的区间，348 个用本结果的完整 tail 交叉 Gram 预算；自适应最大实际深度为 2。最坏子片现在位于前缀原元素 17，采用原 R236 途径。新的完整 tail 途径解决了原 R236 因 \(d_0+2p\) 而失守的尾部大微分区。

与同一场 R251 的全时几何证书合用，当前场具有完整连续 metric、reach、held、嵌入及含反射非全等的已登记保证。本结果不声称连续上界优于旧 R245 的另一场，不声称准确等距，也不把这一个场或一次新步称为完成 README #5 的同 g 真实加密收敛。

## 1. 保留准确源的分解

尾部原 X 的定义为旋转背景加完整有限 Fourier 扰动：

\[
X=B+V,\qquad
B(r,u)=(r\cos u,r\sin u,z(r)),\qquad z_r=-w(r).
\]

物理 s 方向从 common cut 指向 cuff，故

\[
r_s=-\frac1{\sqrt{1+w^2}},\qquad
B_s=\frac{-e_r+w e_z}{\sqrt{1+w^2}},\qquad
\frac{B_u}{r}=e_\theta.
\]

背景 B 对原尾部目标 \(g=ds^2+r^2du^2\) 准确等距。C 的支撑仅在中央首 ramp，故在本节的整个尾部 C 恒为零。

记目标正交标架中的 W 微分矩阵为

\[
D=(W_s,W_u/r),\qquad p\ge\|D\|_F.
\]

此次 p 直接使用该实际场已完成 R236 报告的全域准确上界：

\[
p=\frac{194035161005049877170227}{39614081257132168796771975168}
\simeq4.898136088164749\times10^{-6}.
\]

R236 的全域量含 C，在尾部 C=0，故可直接作为 W 的上界。原 R21 已付

\[
\|g^{-1/2}(X^*\delta-g)g^{-1/2}\|_{\rm op}\le d_0,
\qquad d_0=\frac{257212}{10^{13}}.
\]

展开同一 g 下的实际 Gram 差，**先保留背景与 W 的全部交叉项**：

\[
E_Y=E_X+L_B+L_V+D^TD,
\quad L_B=D_B^TD+D^TD_B,
\quad L_V=D_V^TD+D^TD_V.
\]

既有准确 Bernstein 源证书给整个有限 tail 加深 collar 的

\[
\|V_r\|\le v_r=\frac{13363861799117558165703}{10^{24}},
\qquad
\|V_u\|\le v_u=\frac{143305659413411896211}{5\cdot10^{22}}.
\]

因此，对一个半径下界 \(r_-\) 的区间，

\[
\|L_V\|_{\rm op}\le2vp,
\qquad
v=\sqrt{v_r^2+(v_u/r_-)^2},
\qquad
\|D^TD\|_{\rm op}\le p^2.
\]

这两项只对小扰动 V 及 W 支付三角不等式；大小为 1 的旋转背景 B 与 W 的抵消在下文完整保留。没有删去 V 的任何高模式。

## 2. 准确材料角与一个小振幅 Laurent 展开

W 的保存角基是中央参数 θ，原尾部 Fourier 源使用真实材料角 u，不能把它们直接当成同一个角。记原中央曲线 \(\gamma(\theta)\) 的速度为 J，准确平均弧长半径为 a，故

\[
\frac{du}{d\theta}=\frac J a,\qquad W_u=\frac aJ W_\theta.
\]

由 R226 已完成的中央弧长与部分原函数证书，令

\[
x=3\theta,
\quad e_0=1-\texttt{central\_original\_chart\_rho\_lower\_exact},
\quad u_0=\theta-\frac{e_0}{3}\sin x,
\quad \rho_0=1-e_0\cos x,
\]

得到

\[
|u-u_0|\le\epsilon_u
=\frac{12673336300281}{5\cdot10^{23}}
=2.5346672600562\times10^{-11}.
\]

这里 e0 由实际中央源的准确二进有理数计算，显示为 0.8。它未被替换成任意拟合常数。R226 还给出准确 \(a_-\le a\le a_+\)、\(J\ge J_-\)、\(\rho_0\ge\rho_->0\)，以及 \(\|J^2-\rho_0^2\|_\infty\le D_0\)。所以

\[
|J-\rho_0|\le H_0=\frac{D_0}{J_-+\rho_-},
\]

\[
\left|\frac aJ-\frac1{\rho_0}\right|
\le\epsilon_A
=\frac{\max(|a_--1|,|a_+-1|)}{J_-}
 +\frac{H_0}{J_-\rho_-}
<6.450688890459\times10^{-8}.
\]

只涉及 B×W 的平面旋转因子有关键形式

\[
e^{-iu_0}W_{xy}(\theta)
=\exp(i\beta\sin x)\sum_m w_m e^{i(m-1)\theta},
\qquad \beta=e_0/3.
\]

全部平面频率满足 \(m\equiv1\pmod3\)，故最后一项是 x 的整数 Laurent 多项式。指数幅度仅 \(\beta\simeq0.2667\)，与 W 的最高 Fourier 模式无关。令

\[
P_{18}(z)=\sum_{n=0}^{18}\frac{[\tfrac\beta2(z-z^{-1})]^n}{n!},
\qquad |z|=1.
\]

所有系数都准确有理，并且

\[
|e^{i\beta\sin x}-P_{18}(e^{ix})|
\le \frac{\beta^{19}}{19!(1-\beta)}
<1.515\times10^{-28}.
\]

证明只用 \(|\sin x|\le1\) 和 \(e^\beta\le(1-\beta)^{-1}\)。这不是有限角度拟合；18 阶之外的无限 Fourier 尾已作为一致余项支付。

将近似背景标架记为 \(D_{B,0}\)，把 W 第二列中的 \(a/J\) 换成 \(1/\rho_0\) 后记为 \(D_0^W\)。旋转矩阵的 Lipschitz 界给

\[
\|D_B-D_{B,0}\|_{\rm op}\le\epsilon_u,
\qquad
\|D-D_0^W\|_{\rm op}\le\epsilon_A\|W_\theta\|/r_-.
\]

因此真实角及速度替换只需另外支付

\[
\|L_B-L_{B,0}\|_{\rm op}
\le2\epsilon_u p+
\frac{2\epsilon_A\|W_\theta\|_\infty}{r_-}.
\]

这里 \(\|W_\theta\|_\infty\) 使用同场 R226 的准确原单位图界，不以有限角观察代替。

## 3. 三项交叉 Gram 的完整 Fourier 分子

设全区间单位径向坐标为 z，材料长度总量为 T，尾部的准确图满足

\[
r=c-hR(t),\quad t=(zT-S)/h,\quad k=R'(t)>0.
\]

于是

\[
W_s=\frac{W_z}{Tk\sqrt{E}},\qquad E=1+w^2.
\]

把平面向量视为复数，定义

\[
A=\Re(e^{-iu_0}W_{z,xy})-wW_{z,z},
\]

\[
B=\Im(e^{-iu_0}W_{\theta,xy}),
\quad A_\theta=\Re(e^{-iu_0}W_{\theta,xy})-wW_{\theta,z},
\quad C_z=\Im(e^{-iu_0}W_{z,xy}).
\]

此处下标 z 在 \(W_{z,xy}\) 表示单位径向导数，在末尾坐标分量 \(W_{z,z}\) 的第二个 z 表示第三笛卡尔分量，代码中分别记作 `height_z`、`height_theta`。

直接点积给出全部三项：

\[
L_{B,0;11}=-\frac{2A}{TkE},\qquad
L_{B,0;22}=\frac{2B}{r\rho_0},
\]

\[
L_{B,0;12}=\frac{N}{Tk\,r\rho_0\sqrt E},
\qquad
\boxed{N=r\rho_0C_z-TkA_\theta.}
\]

尤其混合分子 N 必须先作完整相减再取界。代码保留所有有符号平面频率、height cosine 通道以及全部卷积产生的频率。A、B 为 cosine 多项式，N 为 sine 多项式；D3 与反射对称允许在 \(x\in[0,\pi]\) 分盒覆盖绝对值，再覆盖整个角圆。

## 4. 径向关联与背景 slope 的准确包络

### 4.1 保存的同一个 W

对保存的 binary64 knots/coefficients 视为其准确二进有理定义，使用 R236 的准确 Boehm 插结提取 degree-5 Bernstein 片。每片 W 及其一阶单位径向导数经升阶后共享同一组 6 个非负且和为 1 的 Bernstein 权。

冻结下文的径向标量后，A、B、N 均对这一对 (W,Wz) 线性。因此每一个子片内部的分子是 6 个控制行相应分子的同权凸组合；对各行包络后取最大即可包含整个子片。不是只验证 6 个径向点，也不是把导数控制与位置控制独立组合后猜测其相关性。

### 4.2 原背景 w(r) 的包络

实际消费既有独立审查的源 primitive：

`2026-11-09-db6f-tail-background-primitive-stable-depth4.json.gz`

SHA256 `28577da04035f91bcd5dc310094d5844347cbeb78d6213dcba0232b62acf56e9`。

完整有限源 calibration SHA256 为 `bcfaba00aec62290b5b29432836c9e76ef6cf0d582b06c046677b0f8688ca9f4`。加载器核对原 primitive 的全部实现身份、定义输入链与原 M12 共享 g 的旧审查记录；不以当前非区间数值背景的 w 值为证书。

对每个准确物理半径区间，`db6f-tail-background-point-lipschitz.py` 只把近似逆当作一个提议源点。它向外包住该点的准确物理 r* 与 w*，再以已证 \(|w_r|<24\)（内侧可用更小的 601/100）乘上完整准确距离，包住整个目标半径区间的 w。所需时这同样覆盖 primitive 最深源点与更深 collar 之间的连接；不声称 depth4 primitive 自身保存了无限深源。再与原已证 \(0\le w\le16/15\) 取交。

T、k、r 的区间来自原 R223/R236 的准确材料图、准确根区间和 Bernstein 取值；不能从浮点图输出减出跨度。

### 4.3 冻结误差明确支付

在一片中取各区间中点 \(r_0,w_0,q_0\)，其中 \(q=Tk\)，半宽记为 \(\Delta r,\Delta w,\Delta q\)，且 \(q\le q_+\)。先在每一共用 Bernstein 行生成

\[
A_0=\Re(e^{-iu_0}W_{z,xy})-w_0W_{z,z},
\]

\[
A_{\theta,0}=\Re(e^{-iu_0}W_{\theta,xy})-w_0W_{\theta,z},
\quad N_0=r_0\rho_0C_z-q_0A_{\theta,0}.
\]

把完整 Fourier 乘积与相减作完，随后才取角区间界。冻结误差为

\[
|A-A_0|\le\Delta w\,\|W_{z,z}\|_\infty,
\]

\[
|N-N_0|\le
\Delta r(1+e_0)\|C_z\|_\infty
+\Delta q\|A_{\theta,0}\|_\infty
+q_+\Delta w\|W_{\theta,z}\|_\infty.
\]

所有这些量在代码中按该行完整 Fourier 的 l1 上界，包括其区间舍入误差。分母一律用该子片和该角盒的严格正下界。

## 5. 角向覆盖与舍入

有限 Laurent/cosine/sine 运算使用分母 \(2^{96}\) 的整数系数。每一次从准确有理系数到整数的舍入差都求准确绝对值和；相加、精确常数缩放及卷积的误差按完整多项式乘法规则传播。指数截断余项加入旋转因子的初始误差。最终系数大小不依赖 binary64 判定。

对每个 \(x\in[0,\pi]\) 的角盒，用既有有理 π 及有余项的 sin/cos 区间计算中心值。在中心作 7 阶 Taylor 多项式，并用完整 Fourier 系数的第 8 阶导数 l1 乘 \(\delta^8/8!\) 作余项，覆盖整盒。总计 128 角盒。sine 与 cosine 的全部导数符号分别处理，不能把 sine 分子当成 cosine 输入。

若包络给出 \(|L_{11}|\le e\)、\(|L_{12}|\le f\)、\(|L_{22}|\le h\)，则对称矩阵的行和界给

\[
\|L_{B,0}\|_{\rm op}\le\max(e,h)+f.
\]

加上第 1、2 节的余项，得到每一 tail 子片的完整上界

\[
\boxed{\epsilon_{\rm tail}
=d_0+\|L_{B,0}\|_{\rm op}+2vp+p^2
+2\epsilon_up+2\epsilon_A\|W_\theta\|_\infty/r_-.}
\]

## 6. 完整域、共同切口与全时

完整运行遍历所有原 Bernstein 元素。只有当准确判据

\[
z_-T_-\ge S_+
\]

成立时，才采用尾部 B+V 分解。所有其余区间（包含可能跨越准确 common cut 的极薄部分）使用原 R236 的全域有效局部转移

\[
\epsilon=d_0+2(1+d_0)p_{\rm local}+p_{\rm local}^2,
\]

其中中央 C 的完整微分预算按原真实支撑是否相交支付。故不存在通过一个浮点交界判定遗漏的缝，也不把尚未证实在 tail 内的区间交给 tail 公式。

当包络超过要求阈值时，代码准确 de Casteljau 二分；每个父片被其两个闭子片覆盖，不漏端点。此次全部节点及所有子片最终通过，实际最大深度仅 2。158 个前缀/交界片还单独给出

\[
p_{\rm prefix}\le\frac{38591978588661399325407}{79228162514264337593543950336}
\simeq4.870992506195414\times10^{-7}.
\]

完整动半面之外，W 在真实 cuff 的 0/1/2 jets 为零，原固定 cuff/caps 沿用同一 g 和既有度量界。按 R234、R251 的同一个完整相位族定义，刚性转动、反射及相应材料角平移保持原 g 和上述 Gram 算子范数。因此这是同一闭曲面族的全域、全时度量上界；没有把两个不同场的预算拼在一起。

## 7. 实际身份、完成状态与复现

| 实际输入/输出 | SHA256 |
|---|---|
| field | `b6425243454a6a019d06a729405b0ebdaa0dbbc68b73b7f62745b1587174be1c` |
| grid | `b01dd07d72c5e6fd29ac2aefd4029717bb41754494335a85bbf34e29aa72387b` |
| solver result | `416d1a541b5ee6ab261b12a097e127e0fb772953060008c844189c450b7ea209` |
| R226 同场报告 | `3684cc00854d38a0a429f7288527b908ba43893b620837c5963a01edfe1772a6` |
| R236 同场报告 | `3c15466dd4975579cf824db05a539c65eed13f62f666d9011d7b020c20e95c80` |
| 原 tail 查询报告 | `7d75c93355fb5b79077c8b606294487c02f591e70e40111cac97abcf924da6d2` |
| 新完整 cross-Gram 消费源码 | `197a6696eae4f14723ef92a09c9543f102c789fef95d02fe1a751075e9d8e28d` |
| 新完整连续报告 | `6a7dc22e0d69a38c45a1e6daa739a13ea7ddbe61c6bf324bc6096a5e01015679` |

新代码为 `scripts/2ecf-m12-tail-cross-gram-budget.py`。完整输出 716,529 bytes，仅为可复现的逐片证明记录，保存在 scratch，不进入 git 或 Release；本记录保存结果与所有必要身份。

另做了生产场上的独立数值接口检查：对 3 个真实元素的 9 个径向位置、每个 513 角点，共 4,617 个点，直接用三维笛卡尔点积构造全部三项交叉 Gram，与新 Fourier 分子式比较，最大差 \(7.3851\times10^{-21}\)；准确 Bernstein 与独立 SciPy 样条一阶导数的最大差 \(3.0705\times10^{-21}\)。该检查自然退出 0，记录 SHA256 为 `08b61bf0768ba2e530b8b3af3a6d0bc7a55bbba146172c8fe09c6712d7d14a47`。它仅是实现交叉核对；连续证书的通过由前述准确区间运算决定。

复现入口（实际场及查询先按相应重生步骤生成）：

```sh
OPENBLAS_NUM_THREADS=1 python scripts/2ecf-m12-tail-cross-gram-budget.py \
  --scripts scripts \
  --data /tmp/m12-prefix-data.npz.gz \
  --field /tmp/h2-cold-cache-01/result.json.field.npz \
  --grid /tmp/h487-base/entire-half-grid.json \
  --result /tmp/h2-cold-cache-01/result.json \
  --correction-bounds /tmp/h2-cold-cache-01/correction-bounds.json \
  --query-report /tmp/h487-base/entire-half-exact-tail-queries.json \
  --fine-metric /tmp/h2-cold-cache-01/metric-budget.json \
  --primitive /tmp/2026-11-09-db6f-tail-background-primitive-stable-depth4.json.gz \
  --full-surface --max-radial-depth 7 \
  --out /tmp/h2-cold-full-cross-gram.json
```

primitive 可从公开历史提交 `aed993f7bd33fc6f545f941171c1b78d67258cca` 的原同名 notes 路径恢复，下载后必须核对以上 SHA256。脚本要求新输出路径，并绑定实际 field、grid、result、R226、R236、query、背景 primitive 的身份。后继场需真实重新消费；本场证书不能自动迁移给 C2 富集或 M48 场。
