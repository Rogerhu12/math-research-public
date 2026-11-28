# R618：从实际19519575继续，消去均值导数中的 Fourier 背景

会话 `Astra-new-mechanism-8cdb3418-20261128`，2026-11-28。
**新求解范围；本地仅源码、原日志与输入解析，没有科学运行。**

## 新输入与保持的对象

来源为run45923793283/job140260374411的实际1次接受态，而不是末未闭trial。
完整原FINAL243899 B、SHA256
`b1367076702c3bade368f30034ac79ff9e510888b0f1909259be8899d52aa84e`
逐字进入新输入；1473项response SHA256
`19519575f7b4a8100cf9813851c258188ad4a0063edad05eb1b5b332b83f2cc7`。
初damping准确继承`3.3333333333333334e-9`，累计接受计数从1开始。
原5400.058385949001秒、2完整Jacobian/QR、3拒绝、末未闭trial及此前
两次入口失败、完整reference账均保留，不把嵌套账重复相加。

同一个固定target86da8c60、参考H与amplitude、全部旧口和真实全平尾不变。
硬tau1不变；1473完整列仍计算，只准确消去$\delta\tau=0$这一列，
1472自由列进入全行QR/SVD。work950×256、121600原位置行、fine1728×512、
mean/core512、全部独立2..48及从属至96的核心模式均保持。

旧场数组、target数组与Jacobian因子没有持久保存；新数学上等价的评价器
必要重建时全部如实计费，不声称复用了不存在的workspace。
原失败来源和固定参考已付口不额外重跑。

## 这次具体改变什么

1. [完整推导](2026-11-28-r618-fourier-centered-implicit-derivatives.md)的
   (3)、(8)先利用实际有限Fourier方向的准确零均值消去背景常数，
   系数从同一个Decimal值状态形成，均值收缩用longdouble。
   完整Jacobian、组合方向限制和可选mean-height参数导数都走这条链。
2. 点值导数按推导(9)完整保留背景和离解$D$项，原两次primitive、行权、
   全部QR/SVD方向与实际非线性接受条件不改。
3. 每个方向记录真正限制步长的均值坐标attainer及其$r,W,c_0,\delta s,\delta s_r$。
   原日志没有这些attainer，故先前巨大比例的具体成因仍须实际新结果区分。
4. 标量根允许隔次区间内Newton候选；隔次二分保证进度。
   小残差只提议小括号，实际两端符号验证后才可通过原绝对坐标宽度门。
   两张原same-sign box、目标分拆和参考误差条件全部保留。
5. 保原5400秒/1800末读出预留/20新接受上限；每次实际trial前和全因子后
   检查solver reserve，防止原第二步试值循环把已声明末读出预留完全吃掉。
   实际科学总时钟仍覆盖未闭工作，不强制裁报5400秒。

这不是改变固定$g$、平滑误差阈值或删去内尾/核心行的策略。
longdouble与Decimal没有支付既有源误差、角均值误差或连续区间证书。
完整fine、双direct、真帽锚和mean-height读出仍沿原路径请求；若未完成，
以真实partial和原成本继续，不授完整资格。

## 文件与发布

- `scripts/r618_fourier_centered_mean_chain_20261128.py`
- `scripts/r618_fourier_centered_model_20261128.py`
- `scripts/r618_fourier_centered_consumers_20261128.py`
- `scripts/r618_actual397_fourier_centered_20261128.py`
- `computations/request-r618-actual397-fourier-centered-20261128.json`
- `.github/workflows/visible-r618-actual397-fourier-centered-20261128.yml`

新request的科学stdin571219 B，SHA256
`bfd9607f6c0162cdbfa62fe0b33b03ec88193f99336c4d2900e963ddb98ca383`。
56个来源绑定及所有sparse路径、四份新源码AST、原source/数学field和
两个失败FINAL与本次完整FINAL的逐字继承已作纯静态核对。
新政策通过源码中纯metadata函数提取，并在原model身份建立前绑定；
没有导入或执行科学模块，也没有修改旧已发布源码或已构造对象的身份。
主线程发布前可把readme-read SHA更新为实际最新值，科学stdin不变。

本scope只尝试取得有分辨率的同度量非零下降。
连续同$g$精化、非圆核心的宏观放大、完整闭面几何与README所有比例仍未完成。
