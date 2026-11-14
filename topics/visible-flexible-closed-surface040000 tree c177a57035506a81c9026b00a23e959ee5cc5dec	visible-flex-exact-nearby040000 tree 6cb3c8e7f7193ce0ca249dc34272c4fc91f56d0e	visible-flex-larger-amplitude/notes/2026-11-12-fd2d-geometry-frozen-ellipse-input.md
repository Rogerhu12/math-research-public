# B=.5 椭圆核的固定度量、准确中央 jet 与尾接口

2026-11-12，constructive_geometry。接 R113，不占用新结果编号。

**当前结论：输入接口已具体化，v1 的真实检验已失败；尚无完整强目标活动核。**
本文件区分准确函数定义、有限线性端口、真实有限 Fourier 检验。
正图或形式 Frenet 恒等式不能代替实际 E、F、G。

## 1. 准确中央椭圆及材料角

固定

\[
A=\frac75,\quad B=\frac12,\quad m=1-B^2/A^2,
\qquad a_0=\frac{2A E(m)}\pi=1.0040828380214688\ldots.
\]

这里 \(E(m)\) 是第二类完全椭圆积分。
令

\[
S(\theta)=A\{E(\theta-\pi/2\mid m)+E(m)\},\qquad
\sigma=S(\theta)/a_0.
\tag{1}
\]

不完全积分按振幅连续延拓，故 S 严格递增，S(0)=0、S(2π)=2πa0。
令 \(\theta(\sigma)=S^{-1}(a_0\sigma)\)，再按 2π 周期延拓。
准确中央圈为

\[
\gamma(\sigma)=(A\cos\theta(\sigma),B\sin\theta(\sigma),0).
\tag{2}
\]

记 \(\ell(\theta)=\sqrt{A^2\sin^2\theta+B^2\cos^2\theta}\)，则

\[
\gamma_\sigma=\frac{a_0}{\ell}\gamma_\theta,
\qquad
\gamma_{\sigma\sigma}=\frac{a_0^2}{\ell^2}\gamma_{\theta\theta}
-\frac{a_0^2\ell_\theta}{\ell^3}\gamma_\theta,
\quad \ell_\theta=\frac{(A^2-B^2)\sin\theta\cos\theta}{\ell}.
\tag{3}
\]

所以 \(|\gamma_\sigma|=a_0\) 准确成立。
初始柱段及中心反射接合使用

\[
X(0,\sigma)=\gamma(\sigma),\quad X_s(0,\sigma)=e_z,
\quad X_{ss}(0,\sigma)=X_{s\sigma}(0,\sigma)=0.
\tag{4}
\]

`ExactEllipse.core(sigma)` 返回 (2)–(4) 和准确角导数的浮点求值。
257 个材料角的输入核对得到速度误差 2.23e-16、弧长反演误差 2.67e-15，
这是数值实现检查；(1)–(4) 给函数本身的定义。

后续相位必须平移 \(\sigma\)，不能平移偏心角 \(\theta\)。
如果有完整共同度量解 \(X^*\)，则

\[
X_t(s,\sigma)=R_z(t)X^*(s,\sigma-t)
\]

具有同一个 \(ds^2+a(s)^2d\sigma^2\)。
准确圆 cuff 上该公式逐点固定，因此才能与 R113 的非轴对称固定帽接合。
完整共同度量解及所需 cuff 两 jet 在这里仍未得到。

## 2. 冻结格式与严格 C² 的定义

主 provider 是 `scripts/fd2d_frozen_ellipse_candidate.py`。
`Candidate(bundle).profile(s)` 给 a、a′、a″，`breaks` 给所有分段点，`end` 给半前缀长度。

v2 格式在相邻节点存**共享**两 jet

\[
(d_j,v_j,c_j),\qquad a(s_j)=a_0+d_j,
\quad a'(s_j)=v_j,\quad a''(s_j)=c_j.
\]

节点数字是固定输入，不随之后的网格、解或求解器反馈改变。
区间长 h、局部变量 u=(s-sj)/h 下，定义

\[
P(u)=d_j+h v_j u+\tfrac12h^2 c_j u^2+C_3u^3+C_4u^4+C_5u^5.
\]

置
\(D=d_{j+1}-d_j-hv_j-h^2c_j/2\)、
\(V=hv_{j+1}-hv_j-h^2c_j\)、\(C=h^2(c_{j+1}-c_j)\)，准确取

\[
C_3=10D-4V+C/2,\quad C_4=-15D+7V-C,\quad C_5=6D-3V+C/2.
\tag{5}
\]

函数是 \(a=a_0+P\)。共享端点两 jet 和 (5) 直接证明跨节点 C²。
多项式系数的浮点求值只是缓存，不能作为各段独立舍入的定义数据。

相位段定义为

\[
a(s)=a(s_0)+\int_{s_0}^s\sin\phi(u)\,du,
\qquad a'=\sin\phi,\quad a''=\cos\phi\,\phi'.
\tag{6}
\]

第一相位段的初始 \(\phi=\arcsin v\)、\(\phi'=c/\cos\phi\) 从上一共享 jet 派生，
后续相位直接继承上一段末相位。转向段端点取 \(\phi'=0\)，
coast 段保持相位，故这些接合也准确 C²。
半径定位的 coast 长度由“下一个转向的准确径向积分”和指定目标半径定义，
不能把先舍入的转向位移再当成一个无关联的常数。
provider 中的固定 Gauss 求积是对 (6) 的数值求值方式。

这些规则证明定义的接合阶数；它们没有证明非线性嵌入、reach 或闭合。

## 3. 真实反馈前缀与谱端问题

`2026-11-12-fd2d-ellipse-b05-safe-prefix-n256.json` 和同名 `-state.npz`
保存从准确椭圆到 s=.25 的实际有限 Fourier 前缀。
这段完整 E、F、G 的相对算子误差为 2.3423e-12，采样曲率≤5.95163，
正图余量≥.578448。
该轨迹选择了新的 a(s)；后续冻结后才能称为同 g 检验。

`2026-11-12-fd2d-ellipse-spectral-endpoint-diagnostics.json` 保存三个实际末状态的分带 Fourier 系数。
无滤波运行在 s=.1101 时，模式 32–96 的最大系数小于 1e-15，
而模式 127 的 y 系数达到 5.425e-9，表明早期增长集中在截断端。
滤波保持 D2 对称后可通过 .25；此时模式 48–64 约 5.86e-14。
但到滤波运行的 s=.38495，模式 32、48、64 的系数分别约 1.14e-5、2.20e-6、5.73e-7，
已是宽带分辨率不足，不能把这次失败也说成单个端模噪声。

`fd2d_fixed_ellipse_flow.py` 读取固定 JSON 并记录其 SHA256。
它用实际投影速度和实际二阶导数算 E、F、G 及广义主曲率；输入 JSON 不会被反馈改变。
目前输出仍是有限网格诊断，不能代替全域连续误差证书。

## 4. v1 完整参数与真实失败记录

v1 JSON：`2026-11-12-fd2d-ellipse-b05-frozen-candidate-v1.json`，
SHA256 `35e68a7e1b942b096c1f955724db59d2fd375cad09a984c91bc64badd8293870`。
原 provider 原样保存在 `fd2d_frozen_ellipse_candidate_v1_snapshot.py`。
v1 记录中各段独立保存的舍入系数只有约 2.23e-16 的 jet 接缝；
它不能被引用为严格 C² 的定义，v2 的共享 jet 规则修正了这一点。
原记录保留以复现实验，不把它追改为成功。

v1 选择柱长 .125、真实反馈前缀 .25、第一次收缩速度 .9、暂停半径 .75，
暂停长度 .08621190949，近水平相位 1.568。
半内蕴长 1.45910034，圆背景连尾高度 1.02924470；这些只是背景预算。

`2026-11-12-fd2d-ellipse-b05-frozen-v1-actual-n256.json` 显示，
在 s=.42077936241012126 第一次转向处达到曲率门 1/.136：

| 量 | 值 |
|---|---:|
| 完整相对度量误差 | 1.12546e-11 |
| 正图余量 | .59966092 |
| a | 1.03521439 |
| a′ | .25360476 |
| a″ | -1.78985944 |
| y 半宽 | .60793535 |
| 中央握持见证距离 | .87929323 |

因此 v1 在仍有很好度量误差时已经触到真实局部曲率预算，而且握持距离小于 .9。
不能将其交给后续 BVP 作为已筛过的强候选。

## 5. cut 的准确参考两 jet

使用固定尾配置 `2026-11-12-fd2d-ellipse-cuff032-cut04-config.json`，准确参考为

\[
r_c=\frac25,\qquad w_c=\frac1{10},\qquad w_r=-\frac74.
\tag{7}
\]

从中央向上 cuff 行进时半径减小，因此

\[
a_c'= -\frac1{\sqrt{1+w_c^2}}=-\frac{10}{\sqrt{101}},
\qquad
a_c''=-\frac{w_cw_r}{(1+w_c^2)^2}=\frac{1750}{10201},
\qquad z_c'=\frac1{\sqrt{101}}.
\tag{8}
\]

数值为 `(.4,-.9950371902099892,.1715518086462112)`，z′≈.09950371902。
末刹车相位取

\[
\phi_c=-\operatorname{atan2}(1,w_c),\qquad
\phi_c'=-w_r/(1+w_c^2)^{3/2}.
\tag{9}
\]

二次相位刹车由起始零相位导数到 (9)，故其长度由两端相位差及末导数准确决定。
尾的 cuff 半径为 .32；有限数值组装给 meridian 长 .08005605867、高度 .0019123775401。
这两个数不是尾的全域严格界。

## 6. 线性端口与非线性 worker 的符号约定

`2026-11-12-fd2d-ellipse-cuff032-cut04-port.json` 是 far=48、每 cell 256 步、
真实 cusp 分段的有限线性端口。

| 材料 Fourier 模态 m | 有限 Dm=∂r hm/hm |
|---|---:|
| 2 | 7.657720764629502 |
| 4 | 32.03323279508542 |
| 6 | 58.32248642397737 |
| 8 | 85.11270532016188 |

这里 r 是**内蕴材料半径**，h 是该材料坐标上的高度 Fourier 系数，
不是对变形后空间 xy 半径重画图得到的高度。
在 prefix 的线性约定
\(\delta X=f\cos(m\sigma)e_r-(f/m)\sin(m\sigma)e_\theta+g\cos(m\sigma)e_z\) 下，

\[
\frac d{ds}\binom fg=\frac1a
\begin{pmatrix}-(m^2-1)a'&-m^2b\\(m^2-1)(a')^2/b&m^2a'\end{pmatrix}\binom fg,
\quad b=\sqrt{1-(a')^2}.
\]

由 \(g_r=g_s/a'\) 及 (8)，尾方向准确转成

\[
\binom{f}{g}\ \parallel\
\binom{-w_c(r_cD_m-m^2)/(m^2-1)}{1}.
\tag{10}
\]

暂停处若 a′=0，则 g 不变、f′=-m²g/a；用尾方向反向传播后，暂停长由
\(T=(f_0G-g_0F)/[(m^2/a)g_0G]\) 给出。
它避免两个巨大前向结果相减，但当前双精度端到端方向残差仍为约 1e-9 至 1e-7，
不足以单独声称精确线性匹配，更不代表非线性或全部模态匹配。

新文件 `2026-11-12-fd2d-ellipse-cuff032-cut04-nonlinear-m4-config.json`
是旧 `950f-tail-port-v3.mjs` 可直接消费的全新配置，M=4、spacing=2、depth=12，
已启用实际 cusp union、checkpoint 保留及真实高度 jet；没有引用旧 warm state。
这个 worker 自身采用正背景斜率 w。上半 prefix 采用负背景 z_r=-w，
所以要做整个 z 坐标反射：上半实际高度系数 g 对应 worker 请求 `height=-g`，
返回的 slope、second、meanSlope、meanSecond 同时乘 -1。
在线性层 Dm 不因这个反射改变。
实际接合仍须重建并比较完整 XYZ 两 jet，不能只比较高度 scalar。

调用环境与命令（从仓库根目录执行）：

```bash
VISIBLE_FLEX_SOURCE_ROOT="$PWD/topics/visible-flexible-closed-surface/repro/source-root" \
CLOSING_TAIL_CACHE="$PWD/topics/visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts" \
node topics/visible-flexible-closed-surface/scripts/950f-tail-port-v3.mjs \
  topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-ellipse-cuff032-cut04-nonlinear-m4-config.json
```

首行 ready 给实际 cut jets 和 linearSlope；随后每行 JSON 请求 `height`、`jacobian`、`audit`。
本轮尚未运行这个新非线性尾，原唯一生产 BVP 保持继续。

## 7. 当前继续位置

`2026-11-12-fd2d-ellipse-b05-fastturn-design-n256.json` 已完成一次更快转向的真实设计。
从 .25 起用 .08 的目标转向，实际曲率控制在 7.1 内；到 s=.33 时
a≈1.0417963、a′≈.1619532、a″≈-2.0766812、y 半宽≈.63256。
其完整度量误差已是 8.69e-7，继而在 s=.34139049 触到 2e-5 门，
没有达到 cut。
这时已观察段需要约 .1932 的附加中央柱长；后续选柱长 .2 仍须检验整个新轨迹。

v2 取这段共享 jet 定义一个固定前缀后，先在同一个输入上提高角分辨率，
分清此处的度量误差与真实曲率/握持限制。
新的同 g 实测结果会加在这里；本文件没有把未完成反馈路径报成完成的强目标。

已经冻结的 v2 文件是 `2026-11-12-fd2d-ellipse-b05-frozen-candidate-v2.json`，
SHA256 `064a7a3bcb7beaaa45bf59e30e0c64be58106a566edfa55d6b3c4bf6480b2ba0`。
它使用柱长 .2、反馈区间 .33 和共享 jet 格式；完整背景延伸到 cut，
半内蕴长 1.60694420，背景连尾高度 1.16871260，有限 m2 暂停长 .07679672815。
其完整相位延伸尚未通过真实几何筛选，当前先在 **同一 JSON** 上检验到 s=.53 的既定前缀。

v2 的所有 Hermite 邻接端点 jet 在输入中完全相同。
这些段的系数绝对值三角和给 \(|a-a_0|\le .037722\)、\(|a'|\le .259415\)；
相位段始终在 \((-\pi/2,\pi/2)\)，最深相位的绝对值为 1.568。
因此这个输入定义的是正则正半径背景；这仍只证明背景度量可用，不证明该度量的强椭圆嵌入存在。

## 8. 已完成的 v2 同 g 检验与新的中央自由度

N512 点值状态的运行在 s=.5093106910 触到 E/F/G=2e-5，尚未到请求的 .53；
当时采样 κ≈7.1482、held 见证距≈.91034、y 半宽≈.61795。
频谱在模式 64 尚约 1.3e-10，而模式 169 的 y 系数已约 4.54e-7，
不能把该数值污染当成准确活动核的几何反例。
完整记录为 `2026-11-12-fd2d-ellipse-b05-frozen-v2-prefix-actual-n512.json` 和同名状态。

随后在**同一个 v2 JSON** 上改用独立 Fourier 系数作为 ODE 状态，
并以 scipy.fft 的长双精度计算帧、角导数、投影和实际第一/二形式。
实际 dtype 为 ODE 与 solve_ivp 输出 `float64`、几何帧 `float128`、FFT `complex256`；
这里的 longdouble 有 63 个显式尾数位，不是任意精度计算。
新方法避免小模态与 O(1) 坐标直接相加，但没有消除正高斯曲率段的 Cauchy 放大。
它在 s=.5257826634 时仍有 E/F/G≈1.6162e-5，随后有限几何的 κ 触到 1/.136 门。
这次也未到 .53，更未完成 v2 后续延伸。
文件为 `2026-11-12-fd2d-ellipse-b05-frozen-v2-spectral-n512.json` 和同名状态，
源为 `fd2d_spectral_ellipse_flow.py`。

仅固定准确椭圆全部初值后再附加 M 个尾条件会失去中央求解自由度。
为此已给出周长**严格不变**的中央支撑族
`h_p=h_ellipse+sum p_j cos(2j phi)`，完整解析参数导数与强中央预算见
`2026-11-12-fd2d-geometry-ellipse-support-family.md` 和 `fd2d_ellipse_support_core.py`。
它允许固定 v2 的 g 进行真正的边值求解；完整 held 保护曲线、窄板、全时 reach 和尾接合仍须实际验证。
