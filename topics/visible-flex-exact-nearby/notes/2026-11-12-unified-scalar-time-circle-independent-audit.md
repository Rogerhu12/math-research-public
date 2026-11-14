# 统一标量时间圆接口的独立审查

2026-11-12，reproduce_newton。完整读核新源码、说明及冻结 native/turn 依赖的相关实现。未发现实质缺口；没有重复两个转折段或普通419的节点计算。

## 绑定版本

- scripts/fourfold_phase_unified_scalar_time_circle.py：SHA256 e00d338b42b4c87281f659930442d08cb697d8c9c6bda44fe2f9858109b73492，23886 B。
- notes/2026-11-12-unified-scalar-time-circle.md：SHA256 abb089bdaa37169de1d8390f5a0bdc6fad554619f9d2074a714f7a5d9c4420e1，8312 B。
- turn01 完整报告 SHA256 df83624c52d32dd745e1532695907417b88ec255a945d8797f2f37292e0a5a22；ordinary419 完整报告 SHA256 4816039b1a4cbc662af7039a10a39c78d922d1ce42dfcbd232649bdb14843505。

## 根、解析芽与时间

对象、真根、准确参数、reference time-grid manifest、分支与 subspan 均被逐项核对。时间是有理数加有理数倍 π，首末端没有先变为 binary64。所选芽仍以 common span 识别；union 中单个芽的解析延拓不会因通过采样而被声明覆盖其他真实实区间。

positive.target(t,R_K) 内部确使用 primitive(t,−R_K)，故 root_K[j] 是 K(t−R_K z) 的系数。J(ρ)=−K(t−ρ)/ρ 的保留系数 −root_K[j+1]/R_K 正确。K(t)=0 来自已有严格根证书，不是把近零常数拟合为零。根处各径向系数严格为实数，因此取其实部不会丢掉真实系数。

正根 germ、负根反射 germ 与同一真根包严格对应。负根的曲率可使用同一个正根 J，几何本身仍在正确的负侧 germ 计算。缓存键包含对象、证书、精度、节点、半径、阶数和根球，不跨目标移用。

## 完整径向尾与平方根支

源码另外在完整 |r−t|≤R_K 上重新支付 a、真实 E 的无零点及 K 模数；它没有只用有限 primitive 的 E。复节点调用 complete_data，保留 E 的复值，只有根处的实径向 jet 使用真实实性。

有限 J 多项式在可能非零的复 ρ/R_K 上直接 Horner 求值，外加 M_K/R_K·q^degree/(1−q) 的完整 Cauchy 尾。再除真实 1+cosη，并检查 Re Q>0 后取主支。结果使用 sinη sqrt(Q)，没有把跨根解析的 sinη 换成绝对值或直接 sqrt(−K)。两侧 r_τ=t sinη 都与物理 τ 的方向一致；外层有符号时间半宽仍由密度构造者另乘。

准确 PiTime η=0 时返回准确零是场公式的恒等式，且该点已在输入的同一无零分母域内。一般浮点接近端点不会触发这条准确零捷径。

## 共享径向预算

复时间盘上的径向偏移公式是 sin/cos 加法式和 cosh/sinh 的完整模数界。以 d_r 同时扩大中心的 R₀ 和 R_E 后，两半径差保持不变，每个节点的原 R₀、R_E 圆盘都包含在中心已付圆盘内。

核对 complete_data 可见，E 各阶误差仍除以节点原来的 self.E_radius^j，而不是扩大中心的半径。X=F_r 的无限 primitive 费用也仍为 ε_F/R₀。回调只复用共同 majorant，不改变准确节点处重算的有限几何；其半径身份 guard 阻止误用另一请求。

整角网格保留全部已存有限 primitive 和 phase 系数。angles≥Q 保证这些模式没有赋值碰撞，真实相位导数乘物理频率 4ik。f_invariants 使用同一 X、相位及其径向/角向导数；点处分母模下界与 finite/无限费用均未省略。

## 范围

输入的 whole-angle/time 域为同一真实解析芽提供 holomorphic 模数；新的区间采样提供该芽上真实无限场的逐节点包络。二者相接后仍需单独支付时间 DFT alias、角 DFT alias、遗漏时间和角模式，才能得到完整 P。已记录的独立时间 jet 重合只作实现核对，说明文档没有把它代替连续域证明。

同样，这个模块不包含真实参考残差、返回图误差或参数变分证书。普通419原三芽输入的身份保持不变；后来得到的 sharp 单芽证书没有被静默嫁接进旧报告。

