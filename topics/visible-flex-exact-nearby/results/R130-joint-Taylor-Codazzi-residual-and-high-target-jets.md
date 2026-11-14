# R130：完整高目标 jet 与径向/角向相关残差验证

2026-11-13，visible-exact-astra-ac0d。

**本篇已实际完成的结论：**对 R125 的原固定目标、完整辅助参数盒和整个实角圆，
一个新的准确有限候选在 $[0,1/1000]$ 上的真实未投影 Riemann 残差满足
$$
\rho_0<0.043535832,\qquad \rho_1<10.648890.
\tag{130.1}
$$
四个完整闭径向盒消费原无穷 primitive 后，R129 逐盒屏障实际给
$$
e_0<3.510082\,10^{-5},\qquad e_1<0.009114290,
\qquad\inf|p-q|>0.2435181277.
\tag{130.2}
$$
这里的误差相对于本篇新候选；它逼近的仍是同一个真实初值分支。
完整 signed-frame 消费也已通过，给同一短环带的明确嵌入和局部曲率界
$8.523482$。R129 已证的宽度 $1/200$ 结论继续有效；本篇的作用是建立并
实际验证更紧的连续残差方法，为更远的真实延拓提供输入。

新候选虽然完整保存到 $r=1/20$，本篇**没有**把该长区间称为已验证的 PDE 解。
全闭面的完成条件也没有因此支付。

## 1. 真实目标的四阶几何导数先于区间评价

新入口 `scripts/fourfold_codazzi_high_target_jets.py` 使用原确切20次 scalar germ，
在完整径向盒上直接生成五行径向导数 $0\le j\le4$。
半宽仍是 $10^{-9}$，中心仍是原准确分数；径向盒不得跨实际共同 germ。

对原有限相位，正弦与余弦导数递推为
$$
S_n=\sum_{j=0}^{n-1}\binom{n-1}{j}C_jb_{n-j},\qquad
C_n=-\sum_{j=0}^{n-1}\binom{n-1}{j}S_jb_{n-j}.
$$
乘积使用准确二项系数 Leibniz 式。这样直接得到原切向 Fourier 系数及同一
真实 primitive 的四阶径向导数，再按
$$
F_j=\sum_{h=0}^j\binom jh a_{j-h}P_h
       +a_j e_x+z_j e_z
$$
恢复原旋转框架内的位置导数。原完整 primitive 的径向 Cauchy 余项对每个
$h$ 分别支付 $h!/R^h$，角导数同样独立支付原角余项；没有从已付两阶误差
外推一个未经计算的四阶误差。

R129 的准确零频卷积及全部尾继续给 $E,E',E''$，并新增
$$
E'''=6\langle F_2\cdot F_3\rangle+2\langle F_1\cdot F_4\rangle.
\tag{130.3}
$$
把 $a_0,\ldots,a_4$、$E_0,\ldots,E_3$ 除以各阶阶乘，按有限形式幂级数的
准确乘法/倒数递推，计算
$$
K=-\frac{a''}{aE}+\frac{a'E'}{2aE^2}
$$
至二阶。因此真正付出 $K''$，同时保留 $\gamma,\gamma',\gamma''$ 和
$\beta,\beta',\beta''$。程序还核对幂级数的 $K,K'$ 与旧准确公式的有向交集
非空；这项交集检查不替代 (130.3) 的完整尾费。

本篇完整 native 报告逐盒保存真实 $K''$ 及其全部输入；残差使用各**整个盒**的
高 jet，不把点值外推到邻域。原 knot 处允许使用所属
germ 的一侧高导数；比较和接续按 R126/R129 的分片积分合同进行。

## 2. 新有限候选及全部混合导数

`notes/2026-11-13-codazzi-dense-r005-n512-candidate.npz.gz` 定义了
$[0,1/20]$ 上75段 degree7 时间多项式及512角模型产生的有限 Fourier 函数。
文件名中的 `r005` 在这份新候选中特指 $.05$。
其 SHA256 为
`1fdb86b3f959cd3137cf06bdbb37637643a1a56143152c7e26b622d7b353dd81`，
大小4151530字节。每个存储 binary64 值解释为准确 dyadic，负频准确共轭，
mean 实值，Nyquist 准确零，所有时间端点共享。

原 producer 未修改，实际执行参数为 `--right 1/20 --angles 512 --max-step .001`，
浮点报告是同前缀 `floating.json`。其有限采样误差只是诊断；新的验证器总是
对这个明确有限函数计算完整真实残差，不假设它解任何投影方程。

本次验证只消费前两个候选段并各分两盒，最后准确裁到 $1/1000$。
径向多项式用 R127 的共享端点形式评价。它的局部形式幂级数精确给出
$$
U_{ij}=\frac{\partial_r^i\partial_\theta^j U}{i!j!},
\qquad 0\le i\le3,\quad0\le j\le6,
\qquad U=\widehat B,\widehat C.
$$
角导数直接乘准确物理频率 $4k$，再除 $j!$；对原系数先微分再转成区间。
所有有限模式、系数舍入和完整实角格都保留。

## 3. 真实残差先运算，再做二维 Taylor 包围

完整残差仍为
$$
R_B=\widehat B_r-\gamma\partial_\theta
       \frac{K+\widehat B^2}{\widehat C}+2\beta\widehat B,
$$
$$
R_C=\widehat C_r-\gamma\widehat B_\theta
       -\beta\left(\frac{K+\widehat B^2}{\widehat C}-\widehat C\right).
\tag{130.4}
$$
在规范化混合 jet 中，乘法就是有限矩形卷积。若 $v=1/u$，则
$$
v_{00}=u_{00}^{-1},\qquad
v_{ij}=-u_{00}^{-1}
 \sum_{\substack{0\le a\le i,\ 0\le b\le j\\(a,b)\ne(0,0)}}
 u_{ab}v_{i-a,j-b}.
\tag{130.5}
$$
该递推不填补未知高 jet；二元运算只取两个已知矩形的交集。
(130.3) 和上一节候选导数恰好给出两残差的完整
$0\le i\le2,0\le j\le3$ 矩形。
始终检查整个盒/角格上的 $\widehat C<0$，所以 (130.5) 是合法真实商法则。

给定径向盒中心 $r_*$、角格中心 $\theta_*$，令
$T_{ij}=\partial_r^i\partial_\theta^jR(r_*,\theta_*)/(i!j!)$。
中心仍保留整个辅助参数盒；不是只取参数中心。
令 $U_{ij}$ 是同一导数在**完整径向盒及完整闭角格**上的有向包围。
径向、角向半宽分别记为 $h_r,h_\theta$。对 $j=0,1$，二维 Taylor 定理沿
连接中心与目标点的线段给
$$
\begin{aligned}
|\partial_\theta^jR|
\le j!\bigg[&|T_{0j}|+h_r|T_{1j}|+(j+1)h_\theta|T_{0,j+1}|\\
 &+h_r^2|U_{2j}|+(j+1)h_rh_\theta|U_{1,j+1}|\\
 &+\frac{(j+1)(j+2)}2h_\theta^2|U_{0,j+2}|\bigg].
\end{aligned}
\tag{130.6}
$$
实际实现保留中心残差区间，先计算其左右端点再加入余项；并与直接整个盒的
另一份合法残差包围取交集。交集为空会拒绝报告，不会删去不利输出。

(130.6) 允许 $R(r_*,\theta_*)$ 及其一阶导数中的真实取消先发生，再对剩余
小量取绝对值；二阶余项仍对整个连续矩形收费。这里没有把有限中心点的
残差直接认作连续残差，也没有通过插值猜测未见高频。

完整角格采用16384个格。有限中点多项式的角变化用一阶局部 Taylor 加
完整二阶 Wiener 余项支付；每个所需导数字段自己的完整误差也独立加入。
高阶数据可以很粗，因为它们只乘 (130.6) 的真实二阶半宽因子。

最后使用 R126.24a–b 将 $R_B,R_C$ 和它们的角导数转换为真实 $R_P,R_Q$。
两个完整 $C^0/C^1$ 残差界同时保留，初误差仍从准确有限腰曲率先作 Fourier
系数差再包围全部实角。

## 4. 实际结果、存在性和几何消费

完整 native 报告为
`notes/2026-11-13-Codazzi-joint-Taylor-r001-v2-native.json`，SHA256
`e155792fae85b10e2ac131337b6cdba8c08236224f58f8105c4f6791b851bd3e`。
实际运行78.87秒，四盒完整覆盖，全部目标/候选分母门通过，得到 (130.1)。
例如第一盒 $|R_B|<0.007307695$；同盒直接不保相关性的包围为
$|R_B|<1.8721841$。两者都合法，后者仍完整留在报告用于比较。

随后原 R129 逐盒消费者已实际运行，给 (130.2)。signed-frame 消费也已通过，
有 $\phi_\theta>0.3141128033$、柱坐标 Jacobian $>0.3465415120$，以及前述
曲率界。报告分别为
`notes/2026-11-13-Codazzi-joint-Taylor-r001-piecewise-native.json` 和
`notes/2026-11-13-Codazzi-joint-Taylor-r001-frame-native.json`。
存在性依旧由已存在局部分支和真实比较继续定理给出，嵌入性依旧使用全局
柱角次数及同柱角下高度严格单调，未把离散 ODE 收敛充当 PDE 存在。

新规范化 jet 程序另与直接符号微分作独立24项核对：对包含径向、角向、
混合项和非恒定分母的准确 dyadic 测试多项式，比较两个残差的全部
$0\le i\le2,0\le j\le3$ 导数。入口为
`scripts/fourfold_codazzi_mixed_jet_identity_check.py`，报告为
`notes/2026-11-13-Codazzi-mixed-jet-identities-native.json`。
这只补充复核 jet 代数，不替代原对象的实际全域残差计算。

## 5. 版本、失败与继续范围

成功 native 版本的验证器 SHA 为
`58378a726662562ded9a328eb037b1d4251efabd36b0886970f8ccd7bb44deeb`；
高目标 provider SHA 为
`ea71aefd62bf0c16c9e9c9fe4a5da5ce95a973cf913825bd875a4ba59fc14168`。
报告还记录原目标、候选及依赖源 SHA。首次原型因 `int / Box` 类型接口错误
在零个盒处退出，其失败报告保留；修正为显式区间单位元后才运行本次完整验证。
没有把那个零盒报告称为成功。

本题目录下的复跑入口是：

```sh
python scripts/fourfold_codazzi_residual_taylor.py \
  --right 1/1000 --subdivide 2 --out /tmp/codazzi-joint-native.json
python scripts/fourfold_codazzi_piecewise_barrier.py \
  --native /tmp/codazzi-joint-native.json \
  --producer scripts/fourfold_codazzi_residual_taylor.py \
  --provider scripts/fourfold_codazzi_high_target_jets.py \
  --candidate notes/2026-11-13-codazzi-dense-r005-n512-candidate.npz.gz \
  --out /tmp/codazzi-joint-barrier.json
python scripts/fourfold_codazzi_signed_frame_embedding.py \
  --native /tmp/codazzi-joint-native.json \
  --barrier /tmp/codazzi-joint-barrier.json --out /tmp/codazzi-joint-frame.json
```

运行环境沿用 R127–R129 的本地 flint 路径和单线程设置。
新长候选的其余区间、转折、正帽、无限尾及最终闭面全部仍需继续实际支付。
