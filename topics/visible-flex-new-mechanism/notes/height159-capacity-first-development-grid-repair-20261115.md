# 容量新增人工的首次失败与仅网格修复

日期：2026-11-15。首次公开 run [43711688885](https://github.com/Rogerhu12/math-research-public/actions/runs/43711688885)，source `e38604f6b658cd3a5cbaa784e62484994806f21d`，job `132804450203`。本次没有执行真实输入恢复、几何、Jacobian、LP、159生产或hold。

## 实际失败

新增 `--check-capacity-only` 进入纯数组检查后，首个 `old.set_fine_pool` 记录原网格坐标时调用冻结 `rows_api.fine_coordinates`，其 `_grid` 拒绝人工网格。原消息是 `complete increasing radial chart from zero and original full uniform angle circle required`。

人工fixture的theta写成 `np.arange(Nt,dtype=float)`；原API准确要求逐值等于 `np.arange(Nt)*2*np.pi/Nt`，且径向至少2点、角向至少4点、径向从0严格递增。首次失败发生在容量比较检查之前，所以不宣9个数组或9个编排检查已通过；新科学阶段也完全未调用。这不改变[原159真实容量失败](height159-prefix-diagnostic-capacity-failure-actual-20261115.md)的结论。

开发失败临时输出12544字节，SHA256 `2a99c15ad77174242695e682dfbdaad57a19203554b7385c8af8d0895c585d94`；metadata回执51258字节，SHA256 `a493cc35af9f08a81b38733c9bdde7dc588dbe9c2d6f63fab1eac1ace44eb808`。37个请求源码身份全部与回执相同。runner实际pull/read `44e6800f451e0ff072ef93033f734cd08f8658e9`，双README无差，随后恢复该请求源用于计算；发布器同样记录该规则提交。没有保存可重算开发payload或artifact。

## 最小修复

只改 `frame_height159_fine_capacity.py` 的 `developer_check` 内六处人工定义：

1. theta使用原API同一个完整均匀圆表达式。
2. 默认3×8例的已知峰从角值7改为其原7号角点 `7*2*pi/8`，行ID与所有检查目的不变。
3. k截断/重复峰例从非法1×2改为合法最小2×4；两个重复峰均位于角点 `2*pi/4`。
4. 该例按相同结构公式的准确上界从16改为52：两度量组、四曲率组各覆盖两径向四角，再加两个峰的两分支。它仍检查k截断和重复峰只减少实际union。

生产 `reserve_initialization`、`initialization_diagnostic` 及其之前全部源码逐字节不变；冻结科学驱动、原setter/initializer/learn、真实98个参数与全部预算/门也不改。根和tail对原三个API及其坐标调用作完整静态对照，确认其它fixture属性和配置键已具备。修复后的helper15150字节，SHA256 `b1e37f22e46845bea2d4ed44a61ae5ca0a1940b3f60285c339eaaf6a7d80b6bd`。

本地仅文本差异和AST语法，没有执行新增检查。下一公开请求执行尚未完成的18个新增检查，全部通过后才进入首次真实新容量159生产及持径。旧15个持径与旧8个诊断检查继续不重复；这不是重跑已经完成的研究。
