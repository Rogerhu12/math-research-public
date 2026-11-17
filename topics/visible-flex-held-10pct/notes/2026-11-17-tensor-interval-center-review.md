# q20 完整 Cartesian tensor 区间证书：中心与嵌入独立复核

复核会话：`literature_mechanisms`。本次只读 checker、现有证书、输入结构与 mpmath 的实际转换源码；没有重跑 843264 盒，也没有修改父会话的代码。

对应文件及 SHA256：

- `tensor_interval_center.py`：`80c4fdf1d6909b3a027ed81831c6ec6ae72f73ceaf9c066705e5bd087ce4846b`。
- `tensor_interval_geometry.py`：`6234c458d303dfd2e47dcf1e1a6ee54a3d466118a8aea4d76f66013154c034e7`。
- `q20_tensor_m24_v2.npz`：`e8d758d74170402e3a3f9a0031a30fd47cc7bed3fc6e67c0fa848c306bf6f315`。
- `q20_tensor_full_interval_v2.json`：`eb7a7e32c1ec0652a0ce7457ac5e52386094bd01cc962c7bbdf6f0c391a4c3d1`。

## 结论与适用对象

在声明的 binary64 有向扩张与 mpmath interval 后端算术前提下，没有发现这次实际输入、零径向二分、完整中心修复的漏包围。此结论针对由文件中 binary64 共享二 jet 和有限 Fourier 系数精确定义、再加解析中心 lift 的显式 C² 带边曲面。它不把采样度量残差升级为严格等距证书，也没有包括闭合尾。

先前外部区间、Hermite/Bernstein、有限求和与主曲率 PSD 审查见同目录 `tensor_interval_geometry_review.md`；以下补齐中心与全域单射。

## 1. 解析 core 与逆函数括区

设 `h(phi)=1+sum c_m cos(m phi)`，`rho=h+h''`，弧长函数

`A(phi)=phi+sum c_m(1-m²)sin(m phi)/m`。

实际 `c_m` 与入口 jets 都从 binary64 精确转为 80 位 mpf；小整数乘法所需位数远低于该精度。全局三角不等式经区间算术给出 `rho>=.32695941829679775>0`。入口角变换 `theta=psi-E0 sin(2psi)/2` 满足 `|E0|<1`，因此 theta 和 A 都严格递增。

`findroot` 只提出候选，未被当成存在性证明。每个候选左右各加减 `1e-45` 后，程序逐一验证

`upper(A(lo)) < lower(theta)`，`lower(A(hi)) > upper(theta)`。

这些严格符号加单调性证明唯一逆像位于所给括区。整角盒的 phi 区间取左端逆像下界和右端逆像上界，故包含盒内所有真实逆像。512 个角盒，每盒左、右、中三个括区，共 1536 次独立符号验证。

已直接检查安装的 `MPIntervalContext.convert`：普通 mpf 及列表两个端点分别按 `round_floor`、`round_ceiling` 转成 iv，没有把高精度括区错误压成最近点。程序先执行 `CoreLiftIntervals(...).all_boxes()`，之后才运行将 iv 精度改成 50 位的外部 `trig_intervals`；故中心括区和 Taylor 计算确在初始化的 70 位区间环境完成。

## 2. 所需三阶 core 导数与入口二 jet 的角链式

记 `er=(cos phi,sin phi,0)`、`et=(-sin phi,cos phi,0)`，gamma 为按 theta 弧长参数的 core。代码使用的三个导数正确：

`gamma_theta=et`，

`gamma_thetatheta=-er/rho`，

`gamma_thetathetatheta=-et/rho²+er rho_phi/rho³`。

中心目标在计算角 psi 下的径向 jets 为

`J0=gamma(theta)`，`J1=e_z`，`J2=b gamma_theta(theta)`，

其中 `r=theta_psi=1-E0 cos(2psi)`、`r'=2E0 sin(2psi)`、`b=theta_ss=-Epp sin(2psi)/2`。J2 包含角 warp 的物理链式项，不能误设为零。其二阶 psi 导数应为

`J2'' = b'' gamma_theta + (2 b' r + b r') gamma_thetatheta + b r² gamma_thetathetatheta`。

代码三个系数与符号均相符；J0 的二阶角导数 `r² gamma_thetatheta+r' gamma_theta` 也相符。有限 Cartesian tensor 入口的 0/1/2 阶角导数在同一 psi 下直接减去，不遗漏 mean z、常数 Fourier 项或二 jet。

## 3. 角 Taylor 余项

每个角盒以精确角中点为展开点，c0、c1 分别包围此处 delta 及 delta'，整个角盒的 delta'' 经上述逆函数括区直接区间包围。半宽从外包围端点差取值再向上舍入，因此不小于真实半宽。对 `t in [-width,width]`，

`delta in c0+t*c1+(t²/2)*whole2`，

`delta' in c1+t*whole2`，`delta'' in whole2`

是逐分量的一维 Taylor 定理包围，不要求各分量共用同一余项点。平方跨零时使用零下界正确。c0/c1 本身是区间而非舍入中点。

输出中最大的盒内 delta'' 包围可达 `.1464257`，比节点残差大很多，但这是保守余项；它并未被偷偷替换为小节点值。全部余项进入后仍通过几何门。

## 4. 径向 Hermite lift 及覆盖

三个 cutoffs 为 `H0=1-10t³+15t⁴-6t⁵`，`H1=t-6t³+8t⁴-3t⁵`，`H2=t²(1-t)³/2`。lift 是

`H0(s/ell) delta0 + ell H1(s/ell) delta1 + ell² H2(s/ell) delta2`。

`lift_weights` 对第 j 个 cutoff 的 d 阶径向导数使用 `ell^(j-d)`，并用区间 Horner 计算导数多项式。阶乘比与半整数系数在此范围精确；负幂通过区间除法计算。字段映射 `(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)` 与几何程序所需 `X,Xs,Xss,Xpsi,Xpsipsi,Xspsi` 一致。

外端 s=ell 三个 cutoff 全部零二 jet，故修复和主体精确 C² 接合。实际 ell=.04 是存储节点；此次不启用径向二分。全域保留 1647 个完整径向区间，乘每象限 512 角盒得到 843264 个盒，含中心，零失败。跨越 ell 的通用分支也把零 lift 纳入包围，不过本次不依赖它。

## 5. 两个新增正下界确能证明全域嵌入

写 `rxy=sqrt(x²+y²)`，`P=x cos(psi)+y sin(psi)`，`J=x ypsi-y xpsi`。证书给出

`P>=.2990704469445402>0`，`J>=.08970962836926409>0`。

P>0 先保证 rxy>0，并使极角差 theta-psi 有唯一连续代表落在 `(-pi/2,pi/2)`，故每个 s 上的角映射 degree 为 1。J>0 给 `theta_psi=J/rxy²>0`，从而每圈的 theta 坐标全局可逆。

把 s 导数改在 theta 固定时取，柱坐标行列式恒等式为

`det[X,Xpsi,Xs] = rxy³ theta_psi * partial_s(z/rxy)|theta = rxy J * partial_s(z/rxy)|theta`。

左端由 `X·(Xpsi cross Xs)>0` 得正，正面积和法线支撑证书已支付此条件。因此 lambda=z/rxy 沿固定 theta 的 s 严格递增。中心解析 core 满足 lambda=0，故上半前缀 s>0 时 z>0。若两个上半点位置相同，其 theta 和 lambda 相同，严格单调性先得 s 相同，再由角逆映射得 psi 相同。于是上半前缀单射。

下半由 z 反射得到，和上半只在 core 相交。精确中心物理二 jet 已使拼接 C²，正面积给浸入；紧致带边参数域上的连续单射给拓扑嵌入。因此这一步证明上下反射的完整前缀是嵌入环带，仍不是闭曲面。

## 6. 已有全域数值界的含义

此次区间输出：`X·n>=.3496741894128246`，`|X|<=1.5089688121746219`，相位 pi/2 witness 距离至少 `.32548271752566243`，面积至少 `.2990595891179857`，两套 `8I +/- II` 的对角元至少 `.692026280569934`、行列式至少 `4.422865495853693`。

这些是显式有限 C² 前缀的连续几何界；曲率、法线支撑、单射与 witness 不依赖将其实际第一基本形式替换成目标 g。真正严格的同一 g 连续族、完整非线性尾、圆领/帽接合仍需分别支付。
