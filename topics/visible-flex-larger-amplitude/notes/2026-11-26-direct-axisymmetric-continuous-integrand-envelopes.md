# Direct R690 单位子午线的连续 integrand 输入包围

这是 R694 低阶积分误差代数所缺的一个完整输入组件。它绑定实际独立 axis 分支的完整 checkpoint、实际报告、准确 reference 与全部来源，返回每个准确径向胞及全角上的

$$
B_j\ge \sup\|\partial_\phi^jT\|,\qquad
L_j\ge \sup\|\partial_s\partial_\phi^jT\|,
\quad j=0,1,2,\quad T=e^{[\omega]_\times}T_0.
$$

这里 T 是完整 hDelta 场中的 integrand；最终场仍是 $F=G+h\Delta$。本组件没有把 T 当成 F_s，也不适用于把 zeroDelta bubble 修正后的新 integrand 冒成同一个 T。总 quadrature、Hermite / scalar / normalization 浮点误差、逆 core 图、完整 Gram 与几何证书仍另付。

完整实现为 scripts/resume_20261126/so3_axisymmetric_continuous_integrand.py。所有科学执行，包括准确整数包围计算，均限制在本公开仓库 Actions。源码 AST/compile 与纯字节检查可以本地进行；本组件没有本地数值 fixture 或未经实际报告绑定的场。

## 一、实际状态和准确数学对象

输入严格接受独立 axis 完整驱动器的真实 schema、完整 source SHA 与全部 source-role 注册。当前使用 v2 provider 4e6557、operator 7f26ff、driver 606e00。四个必要 source pins 还包括 R694 低阶核 30ae7d；provider 内原7角色和 driver 全来源也逐字核验。

--state final 要求实际完整完成报告及该 final_bundle_sha256。--state initial 则要求真实 initial_new_bundle 与初场读数，明确选择该初场；不会把后来的 final metrics 贴到初场。读取全部 omega_jets、core、H、mesh、fixed_chart_core 和 complete model，比较真实报告、bundle和reference的全部身份。固定端口槽、当前前三core值和完整尺寸必须相符。

准确径向域是 reference 原节点报告中的 affine-in-S 节点
$s_j=\alpha_jS+\beta_j$，不是数值 mesh 数组所组成的另一个定义。准确 omega 是 checkpoint 的 binary64 节点值、一二阶物理 s 导数作为精确有理输入，在此准确域上的唯一 shared quintic。数值 operator 通过 carrier mesh 的 Hermite 求值与该准确对象之间的差，属于后续求值误差，未在此默认为零。

chart 始终是固定初始 core 的 $\theta_0(\phi)=\Theta_{c_0}(\phi)$。当前自由 core 和 H 随完整 checkpoint 一起绑定，但不替换这个 chart。当前 core 的逆图误差属于 Gamma 项，而非此 T0 参考的角导数。

## 二、整个准确子胞的标量分片

对子胞 $u\in[u_0,u_1]\subset[0,1]$，准确左右端点仍是 affine-in-S。分别用同准确 S 盒计算两端 s 包围，并在减法前消掉 affine 系数，得到 t=S−s 的两端范围。尤其尾部两端都含同一个 S 时，宽度先化简为准确常数；不能先把两个独立 S 浮点盒相减而引入虚假的窄胞宽度损失。

ScalarWholeInterval.enclose(left,right) 对整个范围作分支交集，随后取并集包围：

1. 在原 quintic prefix 上，使用原准确多项式计算 b=a_s、b_s，并使用已证的全 prefix $|b|<1$ 正隙计算 $c=\sqrt{1-b^2}$、$c_s=-bb_s/c$。
2. 在原解析段上使用同准确 $\alpha_s=-K$，计算 $b=\sin\alpha,c=\cos\alpha,b_s=-Kc,c_s=Kb$。
3. 在完整 Hold 上，对每个原段端点盒形成与查询范围的安全交集，消费 e091 的原 _old_angle_curvature。
4. 在 $0\le t\le d/4$ 的完整新尾上，调用相同准确 beta_and_curvature 对整个 t/d 区间求包围，包含 cutoff 以下所有无限尾，再计算 $b=-\cos\beta,c=\sin\beta,b_s=-K\sin\beta,c_s=-K\cos\beta$。

新旧边界可以同时贡献；以 hull 合并，不能只按一个浮点中点决定分片。没有把 provider 的准确 affine 单点盒误称为整个胞的包围。

### 原 Hold helper 对整个区间为什么仍有效

该 helper 在查询盒接触某个段边界时，以该准确边界相位和曲率为基点，支付

$$
|\alpha_s|\le 5/2,\qquad
|K_s|\le \frac{4653}{1000}\frac{15}{8f},
$$

其中 f 是原准确二进制 fall width。前者来自原各 ramp/plateau 的范围，后者来自 S5 导数最大值15/8、第一段最大曲率差严格小于4653/1000，以及其余更缓的段。界跨各光滑连接保持有效。

若边界盒为[$\ell,r$]、查询盒为[$a,b$]，helper 使用
$\max(|a-r|,|b-\ell|)$作为距离费用。这同时覆盖查询区间每个真实 s 和盒内真实边界。因此即使一个查询范围接触多个边界，取第一个边界给出的全局 Lipschitz 包围仍有效，只会更宽。若没有接触边界，查询盒整体位于同一段，原 constant / ramp 公式及中点Lipschitz费用适用。

实现还将 K 与已证全 Hold 的[-5/2,5/2]相交。这是同函数的既有准确范围，不是把样本剪成所需结论。prefix 的正隙也来自原 oracle 的完整 Bernstein bound。靠近新帽端使用稳定 sin(beta)/cos(beta)，不以消减后的浮点 $1-b^2$ 替代 c。

## 三、固定 chart 的全角界与准确单位 T0

令 $\nu_m=2m$，初始完整 core 系数为 $c_{0,m}$。直接使用所有160项的有理 L1 界：

$$
R_0=1+\sum_m |(1-\nu_m^2)c_{0,m}|,\qquad
R_1=\sum_m|\nu_m(1-\nu_m^2)c_{0,m}|.
$$

于是对所有角有 $|\rho_0|\le R_0$、$|\rho_0'|\le R_1$。这里只用了完整有限 Fourier 公式和 $|\sin|,|\cos|\le1$，没有临时造角网格。另记录 $1-\sum|(1-\nu_m^2)c_{0,m}|$；仅当它为正时才能用该三角下界证明固定 chart 的 rho0 正性，不能转给当前移动 core。

准确参考

$$
U=T_0=b e_r(\theta_0)+c e_z,\qquad b^2+c^2=1
$$

的 norm 恒为1。若整个子胞有 $|b|\le B$、$|b_s|\le B_s$、$|c_s|\le C_s$，令
$A_2=\sqrt{R_1^2+R_0^4}$，则可取

$$
\begin{aligned}
\|U_s\|&\le\sqrt{B_s^2+C_s^2},&
\|U_\phi\|&\le BR_0,&
\|U_{\phi\phi}\|&\le BA_2,\\
\|U_{s\phi}\|&\le B_sR_0,&
\|U_{s\phi\phi}\|&\le B_sA_2.
\end{aligned}
$$

这里第二角导数的两个项沿 $e_r,e_\theta$ 正交，故使用平方和。radial s 导数只替换 b为b_s，固定chart不随s变化。所有平方根以R694的准确有理 dyadic upper sqrt求上界。

不使用旧 normalized-parent 的正范数下界 nu 或其 D²N、D³N 放大因子，因为准确 U 已有直接单位定义。数值 provider 对其 b,c carriers 进行的归一仍有待支付的浮点费用；这一简化不把数值归一误差宣布为零。

## 四、准确物理宽度上的 omega quintic

对一个 cell，准确宽度 $h=s_{j+1}-s_j$ 先按 affine 系数相减，再包围，必须有正下界。每个旋转标量通道的六个端点 jet记为 $y_0,u_0,a_0,y_1,u_1,a_1$。在 t=(s−s_j)/h 坐标写多项式 $p(t)=\sum_{k=0}^5c_kt^k$，取

$$
c_0=y_0,\quad c_1=hu_0,\quad c_2=h^2a_0/2,
$$
$$
e_0=y_1-c_0-c_1-c_2,\quad
e_1=hu_1-c_1-2c_2,\quad e_2=h^2a_1-2c_2,
$$
$$
c_3=10e_0-4e_1+e_2/2,\quad
c_4=-15e_0+7e_1-e_2,\quad
c_5=6e_0-3e_1+e_2/2.
$$

每个运算都是 e091 固定整数 scale 下的有向包围，binary64端点 jet按其准确有理字面读取。重复 h 的依赖没有被当成独立真实变量；忽略相关性只放宽盒，不改变真实包含。物理导数系数是 $(k+1)c_{k+1}/h$，除数使用同准确正 h 盒。

在子区间 $t=a+(b-a)\xi$ 上先完整平移 / 缩放 power 系数，再转 Bernstein：

$$
\tilde c_k=(b-a)^k\sum_{j=k}^d {j\choose k}a^{j-k}c_j,\qquad
\beta_i=\sum_{k=0}^i\frac{{i\choose k}}{{d\choose k}}\tilde c_k.
$$

Bernstein非负分割性给出整个子区间的凸包包围。这个过程保留原高阶系数之间的端点消减；没有把 power 系数的粗L1和当成全径向范围，也没有只读取节点值。

源码支持默认每胞一个完整区间，以及显式更多等分准确子区间。对子区间内系数再取界不会改变 omega 试探空间或固定问题。

## 五、全 Fourier 旋转界与 R694 接口

omega 的实际 world通道是：

- x：sin((2m+1)phi), m=0..M；
- y：cos((2m+1)phi), m=0..M；
- z：sin(2m phi), m=1..M。

对每个 world通道分别汇总全部482标量径向多项式在该子区间的范围绝对值；第j个角导数乘实际频率的j次方。分别得到 $(r,j)\in\{0,1\}\times\{0,1,2\}$ 的三通道L1界，再取三分量平方和的准确上平方根，得到 $\omega_s,\omega_\phi,\omega_{\phi\phi},\omega_{s\phi},\omega_{s\phi\phi}$ 的全角范数界。

这些量直接喂给30ae R694 rotation_jet_bounds和meridian_jet_bounds。R694的全局 skew exponential Frechet范数界不要求omega很小，也不删除绕T0的规范方向。得到每子区间的三B/L后，再取全cell最大值，所以每条返回record确实覆盖整个准确cell和所有角。

本组件不需要 a的第三径向导数、旧父Fsss或omega三阶径向导数。需要的是实际 finite Fourier/shared-quintic 模型已经具备的经典混合角jets。

## 六、完整绑定、自然journal与CLI

CLI要求 --repo、--report、--checkpoint、--reference-bundle、--carrier、--node-report、--scalar-input、--preparation-report、--outdir。可选 --state initial|final、--panels128、--subdivisions1、--admission-seconds600、--resume。

原始cells.jsonl和report.json只留runner。每个完成cell完整记录准确端点、scalar分支、四scalar jet盒、所有omega/rotation/reference bounds与三B/L，保存来源身份与前向hash链。admission仅在完整cell之间自然返回；没有截断一个cell后称其通过。报告明确 completed_cells/total_cells，只有全922cell齐全时 complete=true和whole_domain_maxima才有值。部分结果只叫processed_cells_maxima。

resume必须是同一输入字节、同一source、同一准确对象与同一subdivision定义，逐条复核已有完整journal链和顺序。允许自然预算反复推进；不因一个600秒预算结束停止研究。可替换代数缓存不属于永久科学位置。

此组件不重新评估完整数值F/J，不重复昂贵旧优化方向。它确实在Actions执行科学连续包围运算，不能把“没有F/J”误写成没有科学计算。

## 七、输出可以和不可以支持什么

返回 Fraction型 B/L可直接作为R694 signed Peano核的输入。调用者仍需给出实际Gauss/Lagrange partial权、非零mass、准确physicalwidth与carrierwidth、实际节点误差、完整求和 / trig / Exp / Hermite / T0归一运算误差，并支付current core逆图和hDelta六jet组合误差，才可进入完整Gram上界。

对zeroDelta分支，先由这套base T_y包围再组合其新的Wz、根和implicit jets误差；不能直接把这里的B/L叫作corrected T的最终界。它们不证明embeddedness、reach、held或Euclidean商振幅，也没有产生闭曲面flex存在结论。

本次静态验证包括完整源码AST/compile及有向运算、wholeinterval分支、Hermite→Bernstein和R694接口的逐式检查。尚未运行该component的科学预算；数值边界大小必须等绑定真实checkpoint的Actions返回。

## 公开完整来源与待用参数

完整source为29047B，SHA256 `a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6`。完整参数 `computations/resume-20261126-axisymmetric-integrand-envelope-first-step.json` 指向同一03的真实606e完整末场；当前仅刊参数，未排科学预算，也未声称该末场已经返回。该组件不以当前粗候选的全域上界认证取代完整非线性求解。
