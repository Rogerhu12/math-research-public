# R134 续篇：真实三阶目标、完整三次模型及无损候选残差

2026-11-13。

**已证明并已执行两盒。** 本篇把同一原固定目标的导数支付到
K'''、γ'''、β'''，以完整三次标量模型接入原清分母多项式代数。
完整1024角有限候选的全部系数经无损分片读取；每个候选接缝及真正
scalar germ接缝均保留。两盒原生验证已完成，完整[0,1/5]运行继续。
本篇不从有限候选或两盒残差推断全.2分支存在。

## 1. 原目标的六个真实径向jet

原目标仍为 E=〈F_r·F_r〉，原完整primitive、全部无限角尾以及
η∈[−10⁻⁹,10⁻⁹]均不变。每个真实common germ内，先对原标量
多项式、sin/cos组合、单位primitive和半径乘积作准确径向微分，
得到 F_j=∂r^jF，j=0,…,5。不是对一个只付低阶误差的数值函数
再作差分或对误差界形式微分。

相同的完整Fourier零卷积给

\[
 E^{(4)}=2\langle F_1,F_5\rangle
          +8\langle F_2,F_4\rangle
          +6\langle F_3,F_3\rangle.                 \tag{T.1}
\]

每个有限零卷积后都加两因子的完整primitive余项。第h径向、q角向
余项仍支付同一Cauchy因子
h!/R^h · q!(4/σ)^q 及所有半径Leibniz项。最高h=5确实参与，
没有把原四阶primitive误差直接当第五阶误差。

令 a_j=a^(j)/j!、e_j=E^(j)/j!。由完整形式幂级数乘法、逆和正平方根，
准确形成

\[
 K=-a''/(aE)+a'E'/(2aE^2),\quad
 \beta=a'/a,\quad\gamma=\sqrt E/a.                  \tag{T.2}
\]

K的三阶系数恰需a^(5)、E^(4)；γ和β的三阶也完整保留。
实际源码逐项核对新级数的0、1、2阶与原独立公式区间overlap，
并把a5、E4、K3、γ3、β3连同全部低阶量写进每个native行。
对正E、a作逆/平方根的原门仍保留。

## 2. 三次标量模型的全部误差

取真闭盒r∈[m−h,m+h]、u=(r−m)/h。对f=K、γ、β，选择准确
dyadic数c0,…,c3，并设

\[
 f_m(u)=c_0+c_1u+c_2u^2+c_3u^3,
\]
\[
 \varepsilon_f=
 |[f(m)]-c_0|+|h[f'(m)]-c_1|
 +|h^2[f''(m)]/2-c_2|
 +|h^3[f'''([m-h,m+h])]/6-c_3|.                    \tag{T.3}
\]

方括号是同一完整参数盒上的真实区间，绝对值取上端点。
Taylor积分余项说明，对整个径向盒及全部η，
|f(r)−f_m(u)|≤εf。u的正负均包括；三阶导数并未假设为常数。
选择最接近区间中心的binary64仅是在选择准确dyadic模型，
所有取整、中心值、中心一二阶以及全盒三阶不确定性均由(T.3)收费。
尤其εf不是仅最后一项的半径。

这个公共标量误差仍在Fourier卷积之外保留，避免把同一个不确定
常数复制成互不相关的全部角模。清分母主多项式使用实际选定的
cj；最后通过原完整εf公式补回真实目标。

## 3. 全部清分母代数和次数

沿用前篇完整恒等式

\[
 N_B=C^2B_r-\gamma[2BB_\theta C-(K+B^2)C_\theta]+2\beta BC^2,
\]
\[
 N_C=CC_r-\gamma CB_\theta-\beta(K+B^2-C^2).           \tag{T.4}
\]

候选B、C仍是完整degree7径向多项式。三次目标模型使NB的径向
次数至多24、NC至多17；全部系数都保留。角次数分别至多3d、2d。
对1024角候选d=511，4096卷积网满足4096>6d，因此无alias。
8192个闭角单元覆盖整个物理四重周期；mean和全部正负模式均保留。

真目标余项、NB/NC的一阶角导数、恢复RB/RC及RP/RQ、直接加权梯度
源SU/SV的公式与前篇完全相同，允许标量模型多一项而无需改变恒等式。
先对完整有限Fourier多项式微分，再折叠径向变化，只有真实有限谱
舍入误差收取Bernstein因子。禁止把已失去频谱信息的公共径向误差
再免费作角微分。

每盒都核负C分母与真K<0。全盒高目标值和同一盒中点模型分别由
原实际provider求得；两者的actual scalar germ必须准确一致。

## 4. 分片身份和完整覆盖

新reader逐段验证压缩SHA、payload SHA、准确offset及完整原gzip SHA，
然后恢复原数组。它不截断Fourier支撑、删除mean或改变任何dyadic。
继承的ExactCandidate.polynomials与原函数是同一个函数对象。

新的径向partition先取每个候选片与所有实际common_cells的交集，
再按指定整数细分。原候选的极短片也保留。逐行检查left=上一right，
且最终准确端点必须等于本次请求端点。每行保存完整目标高jet、
所有标量模型余项、全部分子界、误差门所需量及actual germ。

新报告使用独立kind
`actual_complete_Codazzi_cubic_target_cleared_polynomial_residual`，
独立source SHA和明确`full_target_cubic_remainder`标记。
没有把新输入改写成旧producer的native；延拓消费者仍须明确消费这个合同。

## 5. 已执行两盒和完整运行状态

两盒覆盖准确区间

\[
 [0,3191982588316895/2305843009213693952].
\]

全η、全角、完整原primitive及全部候选系数均参与，failure=null。
第一盒ρ0<.000066862152、ρ1<.024049633；第二盒
ρ0<.000292151420、ρ1<.126325444。它们是完整闭盒界，
不能与21个径向点的浮点残差直接等同。无延拓/几何结论由这两个数自动产生。

源码和native固定为：

- `scripts/fourfold_codazzi_cubic_target_jets.py`：
  `eb3fe6833fcba0162724031905964563e3f96f77aaa56b7996aadf3856ca8412`。
- `scripts/fourfold_codazzi_cubic_cleared_residual.py`：
  `02c9106751992cd466ac82fea138e4ec5cb0da34eea838b515b1bea4f44e1b5b`。
- `notes/2026-11-13-Codazzi-cubic-cleared-first-two-native.json.gz`：
  `66d1803c8842d294c8dbbba0e5fd5e9f309b107691728fb882a52f0474b59c2d`。

独立审阅已核(T.1)、最高jet阶数、完整Taylor费用、分子次数和
所有germ/候选接缝交集；两个实际盒也已原生跑通。完整[0,1/5]
使用相同已冻结source继续运行，输出另一路径。后续只按实际通过的
C0延拓门作证明，所有失败与未通过区间保持原样。

复现完整输入时运行：

```bash
python scripts/fourfold_codazzi_cubic_cleared_residual.py \
  --candidate notes/2026-11-13-codazzi-dense-r02-n1024-candidate-shards.json \
  --right 1/5 --rows 2 --out /tmp/cubic-cleared-first-two.json.gz
```

去掉`--rows 2`才是完整.2任务。使用HANDOFF的python-deps和单线程设置，
新输出路径是强制要求。主课题的闭面匹配及同族全部完成条件仍未闭合。
