SKU问题

- [ ] 上传图片可以上传多张吗？最多上传几张？

- [ ] 新增SKU的名字是自己输入的？还是自动生成的？截图中没有看到SKU命名，只有SKU简称，在编辑SKU的截图中，SKU名称是不可编辑状态。

- [ ] SPU相关解释及使用规则？

- [ ] UPC相关解释及使用规则？

仓库问题

- [ ] 新增货位中，库区类型里面写的什么？

- [ ] 货列编号，货架编号等，有两个录入数字的位置，最终形态是什么样的？

- [ ] 编号，层号，格号是什么关系？编号是持续的吗？

客户资料

- [ ] 所属部门，所属销售，所属客服，是平台的人？还是客户的人？

- [ ] 客户所属仓库中的运营类型，是根据客户属性自动判断？还是根据仓属性自动判断？还是要手动填写？

承运商

- [ ] 惩罚比例规则？是数字？

拣货箱

- [ ] 拣货箱和库区库位的关系？

和库区库位的关系？

角色互斥

- [ ] 角色互斥怎么操作，起什么作用？

数据字典

- [ ] 数据字典是干什么的？

拣货箱

- [ ] 需要一个具体解释，及关系

库存规则

- [ ] 需要具体关联说明

角色

- [ ] 角色中的权限标识中都有什么权限？互斥吗？多选吗？

接口API备案说明

> <mark>添加部门接口      /department/add</mark>
> 
> {"pid": "0", "deptype": 0, "depcode": "xxx", "name": "xxx", "responser": "id", "email": "xxx", "phone": "xxx", "dispindex": 0, "active": 0, "memo": "xxx"}
> 
> EXP:
> 
> {"pid": "0", "deptype": 0, "depcode": "xxx", "name": "xxx", "responser": "id", "email": "xxx", "phone": "xxx", "dispindex": 0, "active": 0, "memo": "xxx"}

> <mark>添加数据字典    /datadict/add</mark>
> 
> {
> 
>     "code": "TEST4",
> 
>     "name": "测试根分类四",
> 
>     "memo": "测试添加根分类四",
> 
>     "pid": "0",
> 
>     "pcode": "根分类"
> 
> }
> 
> code：分类编码
> 
> name：分类名称
> 
> memo：分类备注
> 
> pid：上级分类ID，0为根分类
> 
> pcode：上级分类编码
> 
> 返回——
> 
> {'code': 200, 'msg': 'ok', 'success': 'AddDepartment', 'data': ''}

> <mark>获取数据字典【分页】    /datadict/pagers</mark>
> 
> page_size=2&page_one=5
> 
> page_size:每页条数
> 
> page_one:页码
> 
> {'code': 200, 'msg': 'ok', 'success': 'AddDepartment', 'data': ''}

> <mark>添加岗位    /post/add</mark>
> 
> {
> 
>     "code": "TEST0",
> 
>     "name": "文员",
> 
>     "memo": "测试添加岗位",
> 
>     "sort": 1,
> 
>     "active": 1
> 
> }
> 
> code: 岗位编码
> 
> name: 岗位名称
> 
> memo: 备注
> 
> sort: 显示顺序
> 
> active: 状态
> 
> {'code': 200, 'msg': 'ok', 'success': 'AddDepartment', 'data': ''}

> <mark>添加角色    /role/add</mark>
> 
> {
> 
>     "name": "TEST0",
> 
>     "tag": "权限标志",
> 
>     "sort": 1,
> 
>     "active": 1,
> 
>     "power": "这里放权限列表",
> 
>     "memo": "备注"
> 
> }
> 
> name: 角色名称
> 
> tag: 权限标志
> 
> sort: 排序
> 
> active: 状态
> 
> power: 菜单访问权限列表   【】
> 
> memo: 备注
> 
> {'code': 200, 'msg': 'ok', 'success': 'AddDepartment', 'data': ''}

> <mark>添加用户    /user/add</mark>
> 
> {
> 
>     "department": "TEST0",
> 
>     "post": "岗位列表【】",
> 
>     "role": "角色列表【】",
> 
>     "account": 1,
> 
>     "email": "42374235@qq.com",
> 
>     "pwd": "Ly818379",
> 
>     "name": "梁晔",
> 
>     "abbname": "lineboy23",
> 
>     "phone": "13810490854",
> 
>     "sex": 1,
> 
>     "active": 1,
> 
>     "memo": "备注信息",
> 
>     "type": "123456"
> 
> }
> 
> department: 所属部门ID
> 
> post: 所属岗位列表【】
> 
> role:所属角色列表【】
> 
> account: 账号
> 
> email:邮箱
> 
> pwd: 密码
> 
> name: 姓名
> 
> abbname: 昵称
> 
> phone: 电话
> 
> sex: 性别
> 
> active: 状态
> 
> memo: 备注说明
> 
> type: 用户类型
> 
> {'code': 200, 'msg': 'ok', 'success': 'AddDepartment', 'data': ''}
