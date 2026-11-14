# R79 后的真实端点类与纯 P1 新目标

日期：2026-11-14。状态：**准确实现与人工开发检查；真实目标尚未运行。**

新脚本 `../scripts/literature_closed_c1_endpoint.py` 导入并绑定旧 C1 producer，不修改此前 95 系数、14 未消项的实际失败输出。它检验的是一个新目标：加入 R79 的真实闭 C1 控制空间后，求完整端点类，再把该类放入真实纯四阶目标。

## 1. 新控制空间来自证明，不来自秩猜测

沿用真实关系 $\omega_s=k_s/(2h)$ 及 R73 的准确分解

$$
\mathcal C_s=D_sP+\mathcal C_3+k_sR(h,k,\omega).
$$

取全部 R71 第三交换子、全部 R77 面积/三次速度系数，以及 R79 两个相容性函数的全部 profile 系数：

$$
\mathcal H=\partial_h(h^2R_h),\qquad
\mathcal K=(R+hR_h)_\omega+2(h^2R_h)_k.
\tag{1}
$$

最后一组由 [R79](../results/R79-closed-horizontal-C1-control-and-endpoint-potential.md) 的真实闭路族、切向跨度与有限维 IFT 得到精确可达性。程序的有理代表秩不承担这项证明。新列没有从实际 profile 值拟合，也不把正则化截秩当函数独立。

仍只编译普通复对角 $\tau(q)=T(q;q,q)$。外槽与内槽不同的完整三线性版本、R78 全相位系统由独立彩色编译处理；本脚本不冒充它。

## 2. 完整端点势代表

设

$$
a=R+hR_h,\qquad b=-h^2R_h.
$$

在 $h=1$ 精确代入，选择基点 $(k_*,\omega_*)=(1,1)$，构造原式代表

$$
F(k,\omega)=\int_1^k a(1,v,1)\,dv
             +2\int_1^\omega b(1,k,u)\,du.
\tag{2}
$$

这两个积分是几何多项式的准确有理积分，不是路径或 profile 的数值求积。所有 $\log h$ 在 $h=1$ 精确为零；不近似计算非有理 $\log h$。

脚本对完整几何表达式逐项验证

$$
R-F_k-\frac{F_\omega}{2h}\in\mathcal W,
\tag{3}
$$

其中 $\mathcal W$ 是第 1 节的实际可达空间。每条通过的行都从原 profile 表达式与原控制列重构，再由新的 IBP/word 实例验证余量为零。

真实 $+1\to-1$ 端口取

$$
(h,k,\omega):(1,1,1)\longrightarrow(1,-1,-1).
$$

对应完整 C1 类的代表是

$$
\tau_{\rm end}=F(-1,-1)-F(1,1).
\tag{4}
$$

两端的 $P_h$ 都用 $h=1$ 零锚，所以原势端差另行准确检查为零。不能将 (4) 先替换成上轮三个 moment 的形式答案。程序单独比较

$$
\tau_{\rm end}-(-4L_--2L_0-4L_+)
$$

在新可达商中的余类，报告一致或仍未找到关系。

若 (3) 未被本次正规化验证，程序仍可输出后续形式检验，但明确 `endpoint_representative_verified_for_true_bridge=false`；不能将纯代数阳性自动称为真实端口结果。

## 3. 真正的新纯四阶检验

令 $A$ 为已经使用的标准正 bulk 二次算子，定义

$$
H_A(\tau)=\frac{D\tau(q)[A(q,q)]-2A(q,\tau(q))}{8}.
\tag{5}
$$

旧 producer 从完整 R56 三角历史先作真实导数、再在常状态置历史值零，给准确互反 bulk 目标 $P_{\rm bulk}$。本次保留它的原身份，求的是

$$
P_{\rm bulk}+H_A(\tau_{\rm end})
+\sum_j c_jH_A(\tau_j)=0,
\qquad \tau_j\in\mathcal W.
\tag{6}
$$

端点项的符号是加号。候选系数先由准确有理消元产生，成功后再从原互反目标、原势、原控制列做一次全函数残差重构。失败不作实际函数非成员证明。

一个实际实现依赖必须保持：旧常态系数提取器会遍历整个系数 DAG，并拒绝一般几何节点。因此默认同时检验 (6) 时，先编常态目标，再编变量几何局部密度；两者仍用同一 profile 代数和右锚。没有改写旧编译器去默默忽略未知几何节点。`--skip-pure-response` 只做 (1)–(4)。

## 4. 输出、人工检查与下一使用

主 JSON 含完整度量无关的算子来源、可达列类别、(3) 全系数结果、(4) 原式与余类、旧三矩比较、(6) 的准确残差及原式复核。关系文件保留有理系数与列来源；可读文件保存端点原式、端点余类和有效纯目标。它们是函数表达式，未生成 profile、候选几何或网格。

人工检查只使用手造多项式势、一个明确可调系数及抽象双线性 $A(f,g)=fg$。检查 $F$ 的两段积分、端口方向、水平导数商身份、$1/8$ 因子和 (6) 的符号，全部通过。没有本地调用真实 local 或 reciprocal compiler。

公开 Actions：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_closed_c1_endpoint.py \
  --out "$VISIBLE_OUT/closed-C1-endpoint.json"
```

默认预算 240 秒、600000 个系数节点、80000 个 profile atoms、100000 个表达式项、300000 次改写及 2 GiB RSS 轮询。预算退出与数学未发现关系分开。所有真实编译只允许在 `Rogerhu12/math-research-public` 的 GitHub Actions。

即使 (3) 与 (6) 都准确通过，结果也只支付真实桥的一条对角纯 $P_1$ 类。完整非对称 $T$、其它相位、$P_0$、逐 $s$ ruling、高阶收敛、有限等距族与宏观闭嵌入完成标准仍未支付。
