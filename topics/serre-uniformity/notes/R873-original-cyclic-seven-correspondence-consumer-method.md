# R873 原循环七对应：十七个真实范数系数的执行契约

本文消费正式 [R873 证明](../results/R873-original-cyclic-seven-correspondence-from-short-section-norms.md)，SHA256 为 `e6401ca85f64c5b9a19afbf9bee2b8f4199864e82eff2e4689bdae882735716f`。首 scope 形成真实原对应的函数域输入，尚不计算原五 Picard 类的活跃支持。

## 1. 身份和范围

核心 `scripts/R873_original_cyclic_seven_correspondence.py`，RESULT `R873-original-cyclic-seven-correspondence`，FINAL `p41-original-cyclic-seven-correspondence-certificate.json`。CLI 为 `--config --retained --output --budget-minutes`。所有新算术仅在本公开仓库 Actions；本地只允许文本、AST、来源和字节检查。

固定原 $p=41$、level82、原 $-3$ 下降、$K=\mathbf Q(s)$、$s^2=-3$，并保持 $\tau=e_0,\ \sigma=e_1+e_{73},\ w_0=e_2$。原 $e_i$ 本身已含 $82^2$，不再补乘或除去该尺度。辅助素数从739顺序搜索，坏约化只产生该素数失败记录，不得写成特征零相关。

输出有两层：十七个完整110项准确整数展开；由实际2058单位子式定义的准确特征零坐标表达式。后一表达式是原准确矩阵的逆作用于原准确右端，没有把模坐标或有理重构候选当成展开坐标。

## 2. 最小真实来源

数学身份保留七组原 producer：R771、R775、R786、R799、R800、R801、R807。每组以原 run/source/core/full manifest、原 certificate/configuration、选中成员逐字节绑定。

R800 的5.5MB旧载体运输 R771 的82条有限 Eisenstein 行和原标签群、R775 的146维 M2 recipe 与40个 determinant cosets，以及 R786 已成 exact E1/M2 前缀。R800 本身只选82条 E1 尾和 M2 编号0、1、2、73的129至195尾。其余原 M2 尾、旧 seed 和旧普通积不重算。

R799 只读原 V8 index 所选2050个完整109项行；R801 只读同序2050行的原109所在尾段与完整 recipe dependency plan。保留原尾文件全部字节，核心仅取第109项，没有生成原110至195。R799 已有2050阶非零子式，但没有保存其逆；本次第一次求该模逆，不称复用不存在的逆。

R837 的29.5MB原输入载体带全部418条原 R786 V2 行。仅把它们与原 R786 metadata 逐原 manifest 合并；R837 是运输来源，不冒充原 R786 producer，也不取395MB全局载体。

R807 只取准确 $\theta$ 及 $\theta(82^6E_6)$ 的962个 V4 坐标。原分母、$\lambda$ 归一、$82^8$ 尺度不变。原 V4/ V8 的单项式叶由已成 R801 plan 解析，不重新计算其普通积。

原 live artifact 若经一次公开纯 IO intake 续传，可只改变 transport 描述；原数学身份、文件字节及选中成员集合均不得改变。新 active carrier 只保存本次真正消费的成员。

## 3. 四条 M2 的新增尾

仅追加原四条 $e_0,e_1,e_2,e_{73}$ 在196至763的568项。源的 exact E1 已有0至195；核心只生成新的 signed-divisor 项，并分别与 R771 的原 mod739 coefficient 比较。

仅按这四条真实 recipe 所需的 seed0与seed3、原126项标签群和40个 determinant cosets 卷积新和区间。每条 E1、每个 seed/coset 和每条 M2 新尾均是独立原子阶段。旧0至195的常数、积或系数不重算。新 M2 全部与 R775 原有限行比较，并核原 $v=\xi_{41}^{-10}q_Y$ 的实圆分运输。

目标 $z$ 的八支原始性使用真正原短行：$\tau_0\ne0,\tau_1=(e_1)_1=(e_{73})_0=0,(e_{73})_1\ne0$。它与真实双陪集的 $\sigma_6$、$\sigma_7$ 结合，不另扫描候选目标函数。

## 4. 十七个范数系数

设 $t^7=q_Y$。有限七支的输入是
$$
T\sigma_6(\tau)(t)-\sigma_6(\sigma)(t)-S\sigma_6(w_0)(t),\qquad S^2=0.
$$
在基 $1,t,\ldots,t^6$ 上的乘法矩阵是七阶；其行列式即真正有限支范数。系数环为 $\mathbf Z[\xi_{41}][q_Y,S]/(q_Y^{110},S^2)$。

使用 $T=0,\ldots,7$ 八个固定节点，每节点采用无除法 Berkowitz，并按末端主子矩阵大小1至7原子保存。常数部分次数至多7，$S$ 部分至多6；八节点完整插值使用整数 falling-factorial 变换，逐项准确除去 $7!$ 并代回所有八节点。环乘法以stride79打包两个已约化的39次 $\xi$ 多项式，截断后立即作 $\Phi_{41}$ 约化，才进入下一次乘法。

再乘无穷支
$$
T\sigma_7(\tau)(q_Y^7)-\sigma_7(\sigma)(q_Y^7)-S\sigma_7(w_0)(q_Y^7).
$$
定义中的 $7^6$ 已准确抵消 $7(1/7)^7$，不是数值近似。得到 $P=F(T,0)$ 的九个系数和 $K=-\partial_SF(T,0)$ 的八个系数，共同尺度为 $82^{16}$，全部保留110项、40个原圆分坐标和20个原实坐标。

## 5. 2050旧列加实际八列

准确目标空间是 $H^0(8H+4E)$，维数2058；$V_8$ 只有2050维。不能假设十七个系数属于 $V_8$。

候选补列依次取 $(82^6E_6)^2v_i,\ v_i\in V_2$。在110项范围内准确等于
$$
82^{12}(1-1008q_Y^{82})v_i.
$$
只有这一新乘法被执行，原 $v_i$ 全部已有。先用原2050选行块及其本次新模逆投影，剩余150行上按原 V2 顺序、32列批次实际选择八个独立方向。批次保存游标、真实原 V2 编号和消元列；不预填编号或秩。

接受必须具有非零八阶 Schur 子式。原2050阶子式与该子式给真实2058阶单位子式。保存两边逆乘回及完整选行，利用已证 RR 维数才认证完整空间基。

十七个 RHS 共用这一个分块逆。模解先单独原子保存，再以100行批次核全部2200行和17列。新算的模坐标是准确特征零表达式在本辅助素数的像，但没有声称特征零坐标已展开。

## 6. 可消费的准确函数表达式

源函数统一写为 $e_i/\tau$。旧2050列是已成 V8 recipe 的八个原 M2 因子的积。八个新列写为
$$
\left(\frac{82^6E_6}{\tau^3}\right)^2\frac{v_i}{\tau^2},
\qquad
\frac{82^6E_6}{\tau^3}
=
\frac{\sum c_k(V_4)_k/\tau^4}{\theta/\tau},
$$
其中 $c_k,\theta$ 逐原 R807 坐标引用，$\theta\ne0$ 已有原源证明。

每个系数的准确常数为同一原整数子式 $A_I^{-1}$ 作用于其已成准确 RHS。因为十七个目标的全局成员资格和完整2058基已独立证明，所选行解就是实际全局系数；没有从一次模回代逆推特征零等式。

由这些实际表达式形成
$$
K(C_7)=K(Y)[U]/(P(U)/a_8),\qquad
\pi_t^*z=U,\qquad \pi_t^*w=K(U)/P'(U).
$$
原八支证明给特征零不可约与可分、$a_8\ne0$。正确的完整曲线是原 $Y$ 在该域中的正规化；本 scope 不声称已物化正规化整基或特殊纤维可分性。后继有限域 Picard 消费仍需其真实良约化及原模型接口。

方向始终保原 R870：$H_7(I)=\operatorname{Nm}_{\pi_t}(\pi_s^*I)$。若实现从源侧八维代数取范数，必须按 R873 (873.22) 插入真正 dual-isogeny involution 及其刚性化纤维同构；不能仅以 Hecke 自伴算子相等替代线丛帧比较。

## 7. 断点、输出和边界

所有数学阶段位于输出根目录 `R873-*.json.gz`，都是同一新 tag 的完成阶段；不改旧 source tag。stage manifest 以实际文件清单哈希命名。预算中断保留每条已成新尾、Berkowitz 子矩阵、插值、补列批次、模逆与全部已成 RHS 核验。续算只接受同 core/proof/helper/原数学输入，预算不进数学 tag。

公共 wrapper 只做标准库 IO/schema/来源运输，不导入数学 core。外层超时为预算加900秒，并在退出后保输入载体、完整 manifest、run/core receipt；没有 core receipt 时如实记录缺失。每个 artifact 只保留一日。源码、参数、纸面证明和简明运行/SHA登记可入 Git；机器回执、向量、矩阵及 raw 仅在活跃 artifact/carrier 续传。

首 scope 成功只认证十七个真实范数系数及原有限对应的准确函数表达式。expanded char0 coefficients、正规化整基、理想范数、Picard 活跃支持、principal calibration、非 $p$ 项、period 和 height 均未计算。后继若在合法良素数上给 R870 指定原类的非零 Picard 见证，才可登记对应活跃块；本次不预填该结论。
