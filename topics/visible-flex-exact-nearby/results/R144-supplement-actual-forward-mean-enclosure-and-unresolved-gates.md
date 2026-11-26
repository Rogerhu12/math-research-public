# R144补篇：实际完整前向均值包围与三项未决门

2026-11-26，visible-exact-astra-198c63d-20261126。

**原raw ac1、nu0、原整个eta区间的一个新完整signed forward目标已完成。三个物理门均为unknown，不是几何反例，也不是存在性证明。该目标现锁定，不再重算。**

## 1. 原目标与真正接续

目标由[原合同](../notes/2026-11-26-R144-forward-mean-retraction-contract.md)定义：固定原完整u和j=v/m，以腰Y(0)=1推进
$$
D'=2\beta\langle u^2\rangle D-\tau R_0,\qquad
D^+=D^--[n],\qquad n=a^2/m^2,\quad Y=n+D.
$$
原全部7721个闭格、6143个mean接口、原完整参数区间及同材料角保持。原scalar-mean Green、原Gamma和任何原producer均只读。

首次run45770488571/1完成6791格后，在宽正区间分母的直接商式产生非finite，保存完整右端state；该实际前缀见[记录](../notes/2026-11-26-R144-forward-mean-retraction-prefix.md)。[续算合同](../notes/2026-11-26-R144-forward-mean-retraction-resume6791-contract.md)只读其全部保存整球，用正端点单调倒数，并只推进未完成的930格。没有重新计算前6791格。

## 2. 实际完整记录

公开 [45772466407/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45772466407)，事件提交abeacb531509950ccc8be445eb95677b59b82c8e。

| 对象 | 完整字节数 | SHA256 |
|---|---:|---|
| forward-mean-retraction.json | 8425 | 7cddc5856510c7e602a2e22d504492c8ab4732f900331c02e646f14b04da1635 |
| execution.json | 11588 | 88042f36cae32cdea7e66726667f35efd9367183ee6f4eb6cb012c210ba940cd |

两文件位于 notes/forward_mean_retraction_ci/run-45772466407-1/。science Git blob为212795a7a61a299289081c7d986ff844fcd2dd54，execution为3a672134092188bcb75b975c2792048284fd3a35。manifest SHA256为f71c080384eac9583eac533cc589be01a29a04d0dd1ce5a7d3912de467a8e87c。

完整科学及execution均complete=true，科学proved=true、failure=null，返回码0。完成公共目标计数1；原成功prefix重算数0，续算930格，最终右端25/8、总7721格/6143接口。实际child wall为0.7259651800000029秒。

13个当前小文本和5个immutable历史原件精确核验，固定320bits。全部原科学调用计数0、数组/Artifact/Release发布数0。原private trace保6791条/19064094B，续段930条/2386437B，仅分别保各自hash与metadata chain；没有声称两个hash可给原内容拼接hash。

## 3. 三个全域门的真实结果

| 保存后读回的门 | 实际值 | 可用结论 |
|---|---|---|
| positive_mean_everywhere | unknown | 全部旧row包围尚不能证明Y全域正，也没有完整negative-Y违例见证。 |
| componentwise_moving_C0_within_1e4 | unknown | 未得到全域正分支的完整v变化upper；没有保存的严格mean-shift违例见证。 |
| outer_mean_unchanged | unknown | 保存的D(R)整球不能判定等于零或严格异于零。 |

首个新未决positivity行是零基6803；这是包围不分符号的位置，不是实际Y过零的证明。全域Y下界record为负，但它仍只是lower bound，不能从它反推真Y为负。certified_negative_Y_witness与certified_violation_witness均为null。原prefix未保存的witness历史仍未知；不把缺项当作不存在。

完整D(R)、Y(R)、G(R)、传播初值、signed bulk、所有接口贡献及全域lower/upper均在上述8425B文件中逐字保存。它们是完成的有向包围，不能只取中心作结论。

## 4. 实际确认的数值表示问题

续算首个未成行6791记录：

- n_positive=true，Y_positive=true；
- old_centered_denominator_contains_zero=true；
- old_quotient_finite=false；
- new_mean_shift_finite=true，并保存严格正的分母lower和完整倒数kernel球。

因此原中断的具体原因已由实际记录确认：宽正因子的中心半径乘积外包包含零，随后商式非finite。新实现以正端点单调式合法包围同一个倒数，没有改变数学问题或缩小原参数域。原接口计数核对后，完成prefix恰为5731、失败行未消费增量0；续算将剩余接口全部计入。

## 5. 后继对象的区分

这次完成的是原全eta、旧整row范围的forward enclosure。它不授予point eta0的真实径向相关积分，不授予连续Qrepair、selected delta*、phase条件、非mean PDE、外帽/height匹配或最终族。

下一输入若使用固定eta0和同一径向Taylor变量，须逐个确认原jet的真实参数域；原whole-eta graft不能仅改标签当point输入。旧已成功point域仅读，真正缺失域另行支付。只有新的完整positivity和C0门成立，才可把重投影作为有用近似中心。当前继续这项新输入和真正低逆，不以本次完整unknown收尾。
